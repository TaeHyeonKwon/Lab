import pandas as pd
import numpy as np
import random
from collections import deque
import tensorflow as tf
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from Dueling_Q_network import Dueling_Q_network



class Agent_new:
    def __init__(self, max_memory, action_size, state_size):
        self.learning_rate = 5E-8
        self.gamma = 0.95
        self.exploration_rate = 1
        self.exploration_min = 0.01
        self.exploration_decay = 0.998
        self.sample_batch_size = 300
        self.memory = deque(maxlen = max_memory)
        self.state_size = state_size
        self.action_size = action_size
        self.action_set = [0,0.25,0.5,0.75,1.0]
        self.predict_action_lst = list()
        self.brain = Dueling_Q_network()
        self.target_brain = Dueling_Q_network()
        self.optimizer = optim.Adam(self.brain.parameters(), lr=self.learning_rate)

    def act(self, state):
        # greedy action
        with torch.no_grad():
            if np.random.rand() < self.exploration_rate:
                rand_action = random.sample(self.action_set, 1)
                return rand_action[0]

            else:
                self.brain.eval()
                q_value = self.brain(torch.tensor(state, dtype=torch.float))
                return self.action_set[q_value.argmax().item()]

    def remember(self, state, action, reward, next_state):
        self.memory.append(np.hstack((state, action, reward, next_state)).tolist())

    def replay(self):
        self.target_brain.eval()
        self.brain.train()
        if self.exploration_rate > self.exploration_min: self.exploration_rate *= self.exploration_decay

        sample_batch = np.asarray(random.sample(self.memory, self.sample_batch_size))
        states = np.array([sample[0:15] for sample in sample_batch])
        action = np.array([sample[15] for sample in sample_batch])
        reward = np.array([sample[16] for sample in sample_batch])
        next_states = np.array([sample[17:] for sample in sample_batch])

        s, a, r, s_prime = torch.tensor(states, dtype=torch.float), torch.tensor(action), \
                          torch.tensor(reward, dtype=torch.float), torch.tensor(next_states,dtype=torch.float)

        a = 4 * a
        a = torch.tensor(a, dtype=torch.int64)
        a = a.view(self.sample_batch_size,1)
        q_s_a = self.brain(s)
        update_q_s_a = q_s_a.gather(1, a)

        q_max_out_brain_index = self.brain(s_prime).argmax(1)
        DDQN_target_value = self.target_brain(s_prime).gather(1, q_max_out_brain_index.unsqueeze(1))

        target = r + self.gamma * DDQN_target_value  # target, r+ gamma * max Q(s`,a`)

        loss = F.smooth_l1_loss(target, update_q_s_a)  # r_gamma*
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
