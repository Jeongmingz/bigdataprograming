# week11_chap_numpy_02
import numpy as np

# dtype 의 기본 값은 float64이다.
n0 = np.zeros(5, dtype=int)
n1 = np.ones(7, dtype=np.int64)
# n2 == n3 같은 의미
n2 = np.arange(3, 40, 3)
n3 = np.array(range(3, 40, 3))


print(type(n1[1]))
print(n0, n1, n2)
print(n3)
