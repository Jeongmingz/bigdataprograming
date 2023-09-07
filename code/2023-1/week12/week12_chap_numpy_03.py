# week12_chap_numpy_03
import numpy as np

# BMI 계산
w = np.array([86, 74, 59, 95, 80, 68])
h = np.array([183, 176, 169, 186, 177, 173]) * 0.01

bmi = w / pow(h, 2)

print(bmi[bmi >= 25])
