import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import copy
import torch
import collections
import random
import numpy as np
import wandb

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



class ReplayBuffer():
    def __init__(self):
        self.buffer = collections.deque(maxlen=50000)

    def put(self,state,action,reward,next_state,done):
        self.buffer.append(np.hstack((state,action,reward,next_state,done)).tolist())

    def sample(self,n,buffer):

        sample_batch = np.asarray(random.sample(buffer, n))
        states = np.array([sample[0:4] for sample in sample_batch])
        action = np.array([sample[4:5] for sample in sample_batch])
        reward = np.array([sample[5:6] for sample in sample_batch])
        next_states = np.array([sample[6:10] for sample in sample_batch])
        done = np.array([sample[10:] for sample in sample_batch])


        return torch.tensor(states, dtype=torch.float), torch.tensor(action, dtype=torch.float),\
                torch.tensor(reward, dtype=torch.float), torch.tensor(next_states, dtype=torch.float), \
               torch.tensor(done, dtype=torch.float)

    def size(self):
        return len(self.buffer)


class Actor(nn.Module):
    def __init__(self):
        super(Actor, self).__init__()
        self.fc1 = nn.Linear(4, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc_mu = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        mu = (torch.tanh(self.fc_mu(x))+1)/2 # Multipled by 2 because the action space of the Pendulum-v0 is [-2,2]
        return mu


class Critic(nn.Module):
    def __init__(self):
        super(Critic, self).__init__()
        self.fc_s = nn.Linear(4, 64)
        self.fc_a = nn.Linear(1, 64)
        self.fc_q = nn.Linear(128, 32)
        self.fc_out = nn.Linear(32, 1)

    def forward(self, x, a):
        h1 = F.relu(self.fc_s(x))
        h2 = F.relu(self.fc_a(a))
        cat = torch.cat([h1, h2], dim=1)
        q = F.relu(self.fc_q(cat))
        q = self.fc_out(q)
        return q


class OrnsteinUhlenbeckNoise:
    def __init__(self, mu):
        self.theta, self.dt, self.sigma = 0.1, 0.01, 0.1
        self.mu = mu
        self.x_prev = np.zeros_like(self.mu)

    def calculate(self):
        x = self.x_prev + self.theta * (self.mu - self.x_prev) * self.dt + \
            self.sigma * np.sqrt(self.dt) * np.random.normal(size=self.mu.shape)
        self.x_prev = x
        return x

class DDPG:
    def __init__(self):
        self.learning_rate = 1e-4
        self.gamma = 1
        self.tau = 0.001
        # self.weight_decay = 1e-2
        self.critic = Critic()
        self.actor = Actor()
        self.replay_buffer = ReplayBuffer()
        self.critic_target = copy.deepcopy(self.critic)
        self.actor_target = copy.deepcopy(self.actor)
        self.actor_optimizer = torch.optim.Adam(self.actor.parameters(), lr=self.learning_rate)
        self.critic_optimizer = torch.optim.Adam(self.critic.parameters(), lr=self.learning_rate)



    def select_action(self,state):
        state = torch.FloatTensor(state.reshape(1, -1)).to(device)  # state tensor 변환
        action = self.actor.forward(x=state)
        action = action.cpu().data.numpy().flatten()  # actor 네트워크로부터 액션을 뽑아내고 numpy로 변환
        return action


    def train(self,replay_buffer):
        # batch_size parameter
        batch_size = 128

        # Sample replay buffer
        state, action, reward, next_state,not_done = self.replay_buffer.sample(batch_size,replay_buffer)

        # Compute the target Q value
        target_Q = self.critic_target(next_state, self.actor_target(next_state))
        target_Q = reward + (not_done * self.gamma * target_Q).detach()


        # Get current Q estimate
        current_Q = self.critic(state, action)

        # Compute critic loss
        critic_loss = F.mse_loss(current_Q, target_Q)

        # Optimize the critic
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        # Compute actor loss
        actor_loss = -self.critic(state, self.actor(state)).mean()

        # Optimize the actor
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

    # def soft_update_critic(self):
        # Update the frozen target models (soft update)
        for param, target_param in zip(self.critic.parameters(), self.critic_target.parameters()):
            target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)
    # def soft_update_actor(self):
        for param, target_param in zip(self.actor.parameters(), self.actor_target.parameters()):
            target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)
