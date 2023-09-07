# save_plt_.py

import numpy as np

print(np.linspace(0, 10, 100))  # 0에서 10까지의 총 100개의 수(균일한 간격) 생성
one_to_ten = np.linspace(0, 10, 100)
ott_reshape = one_to_ten.reshape(10,5,2)
print(ott_reshape.shape)
temp = np.logspace(0, 5, num=10)  # log 스케일 수 생성, 10의 0승 부터 10의 5승 사이의 수 10개(기본값 50) 추출
# print(temp, temp[-1])


# 배열의 형태 변형 함수 reshape
# y = np.array(range(12))  # y = np.arange(12)
# print(y)
# y2d = y.reshape(4, 3)
# print(y2d)
# y3d = y.reshape(2, 3, 2)
# print(y3d)
# y_auto = y.reshape(3, -1)  # 행 값을 첫 번째 인수로 주고 열 값은 -1로 하면 열의 개수가 자동으로 맞추어진다
# print(y_auto)


# 평탄화 함수 flatten
# y = np.arange(12)
# y2d = y.reshape(4, -1)
# flatten_y = y2d.flatten()
# print(y2d, flatten_y)
