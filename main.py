from datetime import datetime
from pathlib import Path
import pandas as pd
import numpy as np
import copy
import os
from ESS_new.Agent_new import Agent_new
from My_Battery import My_Battery
from collections import deque
import time


import matplotlib.pyplot as plt

class Main:
    def __init__(self):
        self.episode = 10000
        self.num_hours = 240
        self.initial_battery = My_Battery()
        self.agent = Agent_new(max_memory=3000, action_size = 5, state_size = 15)
        self.train_gap = 10
        self.tou_table = pd.read_csv('TOU.csv', header=None)
        self.reward_lst = deque(maxlen=self.num_hours)
        self.reward_lst_avg = list()

        self.experiment_id = datetime.now().strftime("%Y_%m_%d_%H_%M")
        self.exp_dir = str(Path(os.getcwd()).parent) + "/experiments/" + self.experiment_id
        print(self.exp_dir)
        os.makedirs(self.exp_dir)
        os.makedirs(self.exp_dir + "/brain")

    def generate_demand(self, noise_factor):
        num_days = int(self.num_hours/24)
        avg_demand = np.tile(np.array([10] * 8 + [100] * 10 + [50] * 4 + [10] * 2), num_days+3)
        actual_demand = avg_demand + \
                        avg_demand * np.random.uniform(-noise_factor, noise_factor, len(avg_demand))
        return actual_demand


    def save_config(self):
        configuration = open(self.exp_dir + "/configuration.txt", "w")
        configuration.write("id: " + self.experiment_id + "\r")
        configuration.write("episodes: " + str(self.episode) + "\r")
        configuration.write("num_hours: " + str(self.num_hours) + "\r")
        configuration.write("learning_rate: " + str(self.agent.learning_rate) + "\r")
        configuration.write("discount_factor: " + str(self.agent.exploration_decay) + "\r")
        configuration.write("exploration_rate: " + str(self.agent.exploration_rate) + "\r")
        configuration.write("epsilon_decay: " + str(self.agent.exploration_decay) + "\r")


    def run(self):
        self.save_config()
        for index_episode in range(self.episode):
            demand_vector = self.generate_demand(noise_factor=0.2)
            battery = copy.deepcopy(self.initial_battery)
            state_soc = battery.state_soc # X_t
            state_max_cap = battery.state_max_capacity  # \tilde{X_t}
            state_hour = 0
            if index_episode % 100 == 99:
                print(datetime.now())
                self.agent.brain.save(self.exp_dir + "/brain/" + str(index_episode), save_format='tf')

            for run_hour in range(self.num_hours):
                # Step 0. Set state vector
                state_upcoming_demand = demand_vector[run_hour:run_hour+12]  # \tilde{D_t}
                state = np.array([state_hour, state_soc, state_max_cap, state_upcoming_demand])  # 1+1+1+12
                state = np.concatenate((state[0:3], state[3])) # flatten state
                current_demand = state_upcoming_demand[0]  # D_t
                # Step 1. Generate action
                action = self.agent.act(state)
                # Step 2. Calculate Transition
                purchase, next_state_soc = battery.soc_transition(action, state_soc, current_demand)  # 양으로 나오고
                next_state_max_cap = battery.cap_transition(next_state_soc)  # 양으로 나옴
                # Step 3. Calculate `next_state`
                next_state_upcoming_demand = demand_vector[run_hour+1:run_hour+13]
                next_state = np.array([(state_hour + 1) % 24, next_state_soc, next_state_max_cap, next_state_upcoming_demand])
                next_state = np.concatenate((next_state[0:3], next_state[3])) #flatten next_state

                # Step 4. Calculate reward
                elec_cost = purchase * self.tou_table.iloc[state_hour, 1]
                dep_cost = (state_max_cap - next_state_max_cap) / state_max_cap * battery.init_price
                reward = - elec_cost - dep_cost
                self.reward_lst.append(reward)
                # Step 5. Remember
                self.agent.remember(state, action, reward, next_state)
                # Step 6. Transition occurs
                if(next_state_soc > state_soc): next_state_soc *= 0.9
                state_soc = next_state_soc
                state_max_cap = next_state_max_cap
                state_hour = (state_hour + 1) % 24

            if len(self.agent.memory) > 1000: self.agent.replay() #if (run_hour + 1) % self.train_gap == 0 else None

            print((f'epsiode: {index_episode}, explore_rate:{self.agent.exploration_rate} , action: , reward: {np.average(self.reward_lst)}'))
            open(self.exp_dir + "/realtime.txt", "a").write("epsiode: " + str(index_episode) + ",  explore_rate: "+ str(self.agent.exploration_rate) +
                ",  avg_rewards: " + str(np.average(self.reward_lst)) + "\r")
            self.reward_lst_avg.append(str(np.average(self.reward_lst))+",")
            print(self.agent.predict_action_lst)
            self.agent.predict_action_lst = list()
            self.reward_lst.clear()
            #for i in battery.list:
            #    print(i)
        #print(self.reward_lst_avg)
        open(self.exp_dir + "/avg_rewards0.txt", "w").write("avg_rewards: " + " ".join(map(str,self.reward_lst_avg)) + "\r")

        os.chdir(self.exp_dir)
        x = list(range(index_episode + 1))
        y = self.reward_lst_avg
        plt.ylim([-14000, -10000])
        plt.scatter(x, y)
        plt.savefig(self.experiment_id + ".png")


if __name__ == '__main__':
    start = time.time()
    Main().run()
