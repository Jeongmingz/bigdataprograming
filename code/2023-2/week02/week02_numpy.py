import numpy as np
import random

# :)
num = int(input('숫자 입력 : '))
list_ = [random.randint(1,100) for _ in range(num)]

ndarray_ = np.array(list_, dtype='int16')
print(ndarray_)
