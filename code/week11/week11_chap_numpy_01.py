# week11_chap_numpy_01
import numpy as np

n1 = np.array([3, 9, 7])
n2 = np.array([[1, 2, 3], [4, 5, '6'], [7, 8, 9]])
n3 = np.array([[[1], [2], [3.]], [[4], [5], [6]], [[7], [8], [9]]])

test = [1, '9', 1111.]
n4 = np.array(test)


print(type(n1), n1)
print(n1[1])               # 0d array, scalar
print()
print(n1.shape, n1.ndim)   # 1d array, vector
print(n2.shape, n2.ndim)   # 2d array, matrix
print(n3.shape, n3.ndim)   # 3d array, tensor
print()
print(n1.size, n2.size, n3.size, n4.size)
print(n1.dtype, n2.dtype, n3.dtype, n4.dtype)
print()
print(n1, n1.itemsize, n1.data)
print(n2, n2.itemsize, n2.data)
print(n3, n3.itemsize, n3.data)
print(n4, n4.itemsize, n4.data)
