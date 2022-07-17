# DDPG (Deep Deterministic Policy Gradient)
+ Paper : [paper](https://arxiv.org/pdf/1509.02971.pdf)


## 목적

+ DQN의 단점인 Discrete action space에서만 동작하는 것을 막기 위해 actor-critic framework를 활용하여 deterministic policy를 학습하면서 continuous space에서 동작이 가능토록 하기 위해 


## 설명 

+ DQN + Actor-Critic

    + DQN과 같이 value estimate network와 그에대한 타켓네트워크를 이용하여 학습을 진행

    + Actor-Critic 처럼 Actor network로 $pi$을 추정하고 액션에 대한 평가를 critic network로 진행 


    
