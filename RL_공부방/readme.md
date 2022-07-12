# Actor-Critic

+ Actor 네트워크와 Critic 네트워크를 따로 가짐 

+ Actor는 $\pi(s,a)$ 를 학습 시키고, Critic은 $V(s)$를 학습시킨다.

    + Actor는 State에 따라서 action($a$)을 softmax를 통해 제안한다. 
    + Critic은 Actor를 통해 제안된 action($a$)을 평가한다.

+ DQN과는 달리 Buffer를 사용하지 않고 매 step마다 update를 진행한다.


# TD3

+ DQN의 속성인 target Q network와 Q network를 두어 지속적으로 업데이트 하는 방식과 Actor-Critic의 방식을 혼합한 알고리즘


