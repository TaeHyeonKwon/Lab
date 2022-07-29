# 구조 

+ 가정집 3개,한전1개 interconnected --> grid 
+ 각 가정마다 전력 demand가 존재, 각각 SMP를 활용하여 전력을 판매가능 또는 linked된 이웃집으로 부터 transition 가능
+ 전력을 송신할때, 나갈때는 100%이나 받는 입장에서 거리에 따라 받는 전력 양이 다름 (한전이 제일 먼곳에 위치)
+ obj.func() = grid내 profit을 maximize 


# notation

+ $PV^{n}_t$ = t시점의 n번 째 집 PV 생산량
+ $U^{n}_t$ = t시점의 n번 째 집 활용할 수 있는 전력량
+ $D^{n}_t$ = t시점의 n번 째 집 전력 수요
+ $\tilde{D}^{n}_t$ = t시점으로 부터 6시간동안의 n번 째 집 전력 수요벡터
+ $h$ = 24시간 단위 현재 시간 
+ $C_h$ = h시간의 전력 단가
+ $S_h$ = h시간의 SMP 단가
+ $T_h$ = h시간의 전력판매 단가(이웃집)
+ $A^{n}_t$ = t 시점의 n번 째 집 행동(SMP에 판매할 양)



# Transition
+ $U^{n}_t = max(PV^{n}_t-D^{n}_t,0)$
+ 
