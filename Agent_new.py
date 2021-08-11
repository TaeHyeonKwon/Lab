import pandas as pd
import numpy as np
import random
from collections import deque
import tensorflow as tf
import numpy as np
from Dueling_Q_network import Dueling_Q_network
from tensorflow.keras.optimizers import Adam
import torch


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


        self.brain.compile(optimizer=Adam(learning_rate=self.learning_rate), loss='mean_squared_error')
        self.target_brain.compile(optimizer=Adam(learning_rate=self.learning_rate), loss='mean_squared_error')


    def act(self, state):
        if np.random.rand()<self.exploration_rate:
            rand_action = random.sample(self.action_set, 1)
            return rand_action[0]
        else:
            state = np.expand_dims(state, axis=0).astype('float32')
            q_value = self.brain.predict(state)
            action_idx = np.argmax(q_value[0])
            self.predict_action_lst.append(action_idx)
            return self.action_set[action_idx]

    def remember(self, state, action, reward, next_state):
        self.memory.append(np.hstack((state, action, reward, next_state)).tolist())

    def replay(self):



        if self.exploration_rate > self.exploration_min: self.exploration_rate *= self.exploration_decay

        sample_batch = np.asarray(random.sample(self.memory, self.sample_batch_size))
        states = np.array([sample[0:15] for sample in sample_batch])
        action = np.array([sample[15] for sample in sample_batch])
        reward = np.array([sample[16] for sample in sample_batch])
        next_states = np.array([sample[17:] for sample in sample_batch])

        #q_pred = self.brain.predict(states)
        #q_next = tf.math.reduce_max(self.target_brain(next_states),axis=1, keepdims=True).numpy()
        #q_target = np.copy(q_pred)

        q_s_a = self.brain(next_states)
        idx = np.argmax(q_s_a, axis=1)
        one_hot_action = tf.one_hot(action * 4, self.action_size)
        q_s_a *= one_hot_action
        print(idx)
        q_target = self.target_brain(next_states)
        q_target = torch.tensor(q_target)
        q_out = q_target.gather(1,idx)
        print(q_out)
        raise 13

        target = reward + self.gamma * np.max(q_target,axis=1)

        self.brain.train_on_batch(states,target)
        #q_target[idx, action[idx]] = reward[idx] + self.gamma * q_next[idx]

        #self.brain.train_on_batch(states,q_target)

        #target = reward + self.gamma * np.max(self.brain.predict(next_states),axis=1) #target = R + gamma*max_a(q_s',a')
        #target = target.reshape((300,1)) * one_hot_action
        #q_s_a_update += target


