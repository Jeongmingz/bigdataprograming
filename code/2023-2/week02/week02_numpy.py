import numpy as np
import pandas as pd

# v = np.array([1, 3, -9, 2], dtype='int32')
v = np.array([[1, 3, -9, 2], [1, 3, -9, 2]], dtype='int32')


print(v.ndim, v.shape, v.data, v.dtype, v.strides)

