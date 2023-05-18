# week12_chap_numpy_04
import numpy as np

scores = np.array([88, 72, 93, 94, 89, 78, 99])

# ndarray indexing
print(scores[2])
print(scores[-2])


# ndarray sliceing
print(scores[2:5])
print(scores[3:])


# comparison
# 점수가 90점 이상인 애들만 찍고 싶다.
y = scores >= 90
print(scores[y])

