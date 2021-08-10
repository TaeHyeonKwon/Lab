import torch.nn as nn
import torch.nn.functional as F


class Dueling_Q_network(nn.Module):
    def __init__(self):
        super(Dueling_Q_network, self).__init__()
        self.fc1 = nn.Linear(15, 128)  # fc1 : state를 받아서, 128개 Output
        self.fc_value = nn.Linear(128,1)  # fc_value : fc1의 128개 Output을 input으로 받아 Value function 게산 , Output 1
        self.fc_advantage = nn.Linear(128,5)  # fc_advatnage : fc1의 128개 Output을 input으로 받아 Advantage function 게산 , Output 4

    def forward(self, x):
        x = F.relu(self.fc1(x))
        value = (self.fc_value(x))
        advantage = (self.fc_advantage(x))

        Average_advantage = advantage.mean()  # Advantage의 평균 계산
        Q = value + advantage - Average_advantage  # 정확한 Advatngae 계산을 강제하기 위한 제약식

        return Q