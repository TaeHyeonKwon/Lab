# DDPG (Deep Deterministic Policy Gradient)
+ Paper : [paper](https://arxiv.org/pdf/1509.02971.pdf)


## 목적

+ DQN의 단점인 Discrete action space에서만 동작하는 것을 막기 위해 actor-critic framework를 활용하여 deterministic policy를 학습하면서 continuous space에서 동작이 가능토록 하기 위해 


## 설명 

+ DDPG = DPG(deterministic + Actor-Critic) + DQN 

## DPG 

+ DQN과 같이 value based 알고리즘은 좋은성능을 보이고 있다. 하지만 continuos action space에는 적용이 되지 않는다는 단점이 있음 

+ Continuous action을 수행할수 있다

+ Deterministic 하기 때문에 exploration이 stochastic policy gradient보다 적어짐 
        
       + Actor-Critic 알고리즘의 framework를 적용해 이 문제를 해결함
       + behavior policy($\beta$)는 exploration을 하게 하고--> Stochastic, target policy($\pi$)를 배우게 함--> Deterministic 
       +  



    + In DQN
        + DQN과 같이 value estimate network와 그에대한 타켓네트워크를 이용하여 학습을 진행
    + In DPG
        + Actor-Critic 처럼 Actor network로 $\pi$을 추정하고 액션에 대한 평가를 critic network로 진행 

+ 안정화 기법

    1. Ornstein-Uhlenback (ou-noise)
        + 액션에 첨가하여 train에 사용, 보다 나은 exploration을 하기 위해서 사용함
        + exploration policy($\mu'$)는 ou-noise를 기존 deterministic policy에 추가하여 만듦
    3. Soft update
        + 학습 중인 네트워크가 target 네트워크를 따라가는 속도를 느리게 함 
    4. Batch Normalization
        + observed low dimension feature vector로 학습을 진행한다면 feature의 scale 차이로 인해 network가 학습하는데에 어려움을 겪음
        + 샘플들을 하나의 minibatch에 넣고 모든 dimension에 대해 normalize 시킴.
 
 + 

    
