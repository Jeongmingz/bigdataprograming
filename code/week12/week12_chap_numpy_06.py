# week12_chap_numpy_06
import numpy as np

# BMI 계산
hw = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73], [86, 74, 59, 95, 80, 68]])


bmi = hw[1] / pow(hw[0], 2)
print(bmi)
