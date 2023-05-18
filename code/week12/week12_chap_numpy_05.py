# week12_chap_numpy_05
import numpy as np

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2d array
# print(type(x))
#
# d2_array = np.array(x)
# print(type(d2_array), d2_array.shape, d2_array.ndim)
#
# # list style
# print(d2_array[2][0])
#
# # numpy style
# print(d2_array[2, 0])
#

d2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(d2[0])
print(d2[::2])
print(d2[::2, ::2])


print(d2[:, 2])
print(d2[1::2, 1::2])
