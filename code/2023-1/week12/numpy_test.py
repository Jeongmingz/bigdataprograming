import numpy as np


# 1. 사람들의 BMI를 계산하라.
hw = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73], [86, 74, 59, 95, 80, 68]])

bmi = hw[1] / pow(hw[0], 2)
print(bmi)

# 2. 사람들의 BMI중 정상, 비만, 저체중의 구역을 정해 출력하라. 저체중 (~22), 정상 (23~24), 비만 (25~)
# using comparison
low_bmi = bmi[bmi < 23]
avg_bmi = bmi[(bmi >= 23) & (bmi < 25)]
high_bmi = bmi[bmi >= 25]

print(low_bmi, avg_bmi, high_bmi)
