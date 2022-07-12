# Policy-gradient

+ reference : https://lilianweng.github.io/posts/2018-04-08-policy-gradient/ , https://talkingaboutme.tistory.com/entry/RL-Policy-Gradient-Algorithms


+ 



# Reinforce

+ monte-carlo policy gradient algorithm = Reinforce

+ 여러번 같은 policy를 수행해서 나온 return값을 sampling해서 $Q^{\pi}(s,a)$를 계산하는 방식



# Actor-Critic

+ Actor 네트워크와 Critic 네트워크를 따로 가짐 

+ Actor는 $\pi(s,a)$ 를 학습 시키고, Critic은 $V(s)$를 학습시킨다.

    + Actor는 State에 따라서 action($a$)을 softmax를 통해 제안한다. 
    + Critic은 Actor를 통해 제안된 action($a$)을 평가한다.

+ DQN과는 달리 Buffer를 사용하지 않고 매 step마다 update를 진행한다.


# DPG

+ paper : http://proceedings.mlr.press/v32/silver14.pdf


# DDPG

+ Deep Deterministic Policy Gradient (DDPG)

+ model-free,off-policy 로 학습하기 때문에 잘못된 행동이 누적되어 학습에 영향을 미치는 경우를 방지한다.

+ DPG(Deterministic Policy Gradient)에 DQN을 결합한 --> model-free,off-policy Actor Critic 알고리즘이다. 

+ Actor와 critic 네트워크를 통해 모델을 학습시키는 데,이 과정 속에서 DQN 방식과 유사하게 target 네트워크를 설정해 기존 네트워크로 하여금 업데이트를 진행하도록 한다. 

# TD3

+ DQN의 속성인 target Q network와 Q network를 두어 지속적으로 업데이트 하는 방식과 Actor-Critic의 방식을 혼합한 알고리즘

    + paper :https://arxiv.org/pdf/1802.09477.pdf




