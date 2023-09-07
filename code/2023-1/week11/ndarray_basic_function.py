# week11_chap_numpy_01
import numpy as np

n1 = np.array([3, 9, 7])
n2 = np.array([[1, 2, 3], [4, 5, '6'], [7, 8, 9]])
n3 = np.array([[[1], [2], [3.]], [[4], [5], [6]], [[7], [8], [9]]])

test = [1, '9', 1111.]
n4 = np.array(test)

# shape : 구성을 알려준다. (,) <-   이 튜플안에 숫자가 몇개 들었는지 에 따라 차원을 알 수 있다.
#                               그 숫자가 의미하는 건 그 차원에 몇개의 item이 있는지다.
#                               return type : tuple
# ndim : 몇 차원인지 리턴.  return type: int
# size : 총 요소의 갯수를 리턴한다. return type: int
# dtype : 해당 array의 요소의 타입을 리턴한다. return type: str
# itemsize : 요소의 메모리 값을 리턴한다.
# data : 시작 주소값 리턴

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
