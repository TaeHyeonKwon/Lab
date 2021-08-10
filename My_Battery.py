import numpy as np

class My_Battery:

    def __init__(self):
        self.init_state_max_capacity = 120  # initial capacity as 120 KW
        self.state_max_capacity = self.init_state_max_capacity
        self.life = 0 # L = 0 is new battery, L=1 is dead battery
        self.state_soc = self.state_max_capacity  # fully charged at initial use
        self.init_price = 15000000  # 15k dollars for a new battery

        self.alpha = 5.75E-2
        self.beta = 121

        self.DOD_coef_1 = 1.40E5
        self.DOD_coef_2 = -5.01E-1
        self.DOD_coef_3 = -1.23E5

        self.SOC_coef = 1.04
        self.SOC_ref = 0.5

        self.temp_coef = 6.93E-2
        self.temp_ref = 25
        self.temp = 20

    def cycle_calculator(self, degradation, tol=1, max_iter=1000):
        #Bisection method
        a = 0
        b = 50000
        life = self.life
        f = lambda i: (1 - self.alpha * np.exp((i) * -self.beta * degradation) - (1 - self.alpha) * np.exp(
            (i) * -degradation)) - life
        for i in range(max_iter):
            m = (a + b) / 2  # Calculate midpoint
            val_f_m = f(m)
            if ((val_f_m == 0) or ((b - a) / 2) < tol): return m
            if (val_f_m * f(a) > 0): a = m
            else: b = m


    def soc_transition(self, action, state_soc, current_demand):  # h,x,x_bar, D_tilde


        min_purchase = max(current_demand - state_soc , 0)
        purchase = min_purchase + action*(self.state_max_capacity-(state_soc-current_demand)-min_purchase)  # P_t
        next_soc = state_soc - current_demand + purchase  # X_{t+1} = X_t - D_t + P_t

        #print status
        # print("+++++++++++++++++++++++++++++++++++++++++++++++")
        # print(f"SOC_TRANS - state_soc: {state_soc}, action: {action}, current_demand: {current_demand}")
        # print(f"SOC_TRANS - next_soc: {next_soc}, purchase: {purchase}")
        # print("+++++++++++++++++++++++++++++++++++++++++++++++")
        return purchase, next_soc  # 양으로 나감

    def cap_transition(self, next_soc):

        #step 1. convert to percentage
        current_soc_pct = self.state_soc/self.state_max_capacity #convert to percentage
        next_soc_pct = next_soc/self.state_max_capacity
        #step 2. calculate stress model
        if(self.state_soc != next_soc):
            soc_stress = np.exp(self.SOC_coef*((current_soc_pct+next_soc_pct)/2)-self.SOC_ref)
            #R로 계산해보니 둘이 같으면 에러가 발생함...그래서 같을때는 그냥 0으로 처리하고 다를 떄는 식을 적용해서 계산해야할듯
            if current_soc_pct != next_soc_pct:
                dod_stress = (self.DOD_coef_1*(abs(next_soc_pct-current_soc_pct)**self.DOD_coef_2)+self.DOD_coef_3)**(-1)
            else: dod_stress = 0
            time_stress = (4.14E-10) * 3600
            temperature_stress = np.exp(self.temp_coef * (self.temp - self.temp_ref) * (self.temp_ref / self.temp))
            #step 3. calculate degradation(f_d)
            calendar_aging = time_stress*soc_stress*temperature_stress
            cycle_aging = 0.5* (dod_stress*soc_stress*temperature_stress)
            degradation = calendar_aging+cycle_aging
            #step 4. calculate appropriate cycle number
            if self.life == 1: cycle = 0 # if battery is new, we can not inverse calculate cycle, set cycle as 0
            else: cycle = self.cycle_calculator(degradation)
            #print(cycle)
            #step 5. update battery life
            # Calculate difference between battery life of cycle t, t+1 and apply to current battery life
            cur_life = (1 - self.alpha * np.exp((cycle) * -self.beta * degradation) - (1 - self.alpha) * np.exp((cycle) * -degradation))
            cycle+=1
            next_life = (1 - self.alpha * np.exp((cycle) * -self.beta * degradation) - (1 - self.alpha) * np.exp((cycle) * -degradation))
            life_to_update = next_life-cur_life
            self.life += life_to_update

        #step 6. update state and convert percent to KW
        self.state_soc = next_soc
        next_max_capacity = (1-self.life)*self.init_state_max_capacity #convert percent to KW
        self.state_max_capacity = next_max_capacity

        # print(f"CAP_TRANS - next_state_max_capacity: {self.state_max_capacity}, current_soc_per: {current_soc_pct}, next_soc_per: {next_soc_pct}")
        # print(f"CAP_TRANS - inverse_calculated_cycle(m):, current_life: {self.life}, next_soc_per: {next_soc_pct}")
        # print("+++++++++++++++++++++++++++++++++++++++++++++++")
        return next_max_capacity   # 양으로 나감
