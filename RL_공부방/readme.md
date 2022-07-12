# Actor-Critic

+ Actor 네트워크와 Critic 네트워크를 따로 가짐 

+ Actor는 $\pi(s,a)$ 를 학습 시키고, Critic은 $V(s)$를 학습시킨다.

    + Actor는 State에 따라서 action($a$)을 softmax를 통해 제안한다. 
    + Critic은 Actor를 통해 제안된 action($a$)을 평가한다.




