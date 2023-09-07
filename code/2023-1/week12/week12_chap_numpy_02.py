# week12_chap_numpy_02
import numpy as np

a1 = np.array(range(1, 11)) + np.array(range(10, 101, 10))

# print(a1, a1.shape, a1.size, a1.ndim)
# 1. 0 ~ 9 까지 정수값 가지는 ndarry
array_a = np.arange(10)
print('1.')
print(array_a)

# 2.
array_b = np.array(range(0, 10))
print('2.')
print(array_b)

# 3.
array_c = np.array(range(0, 10, 2))
print('3.')
print(array_c)

# 4.
print('4.')
print(array_c.shape, array_c.ndim, array_c.dtype, array_c.size, array_c.itemsize)

# 5. 직원 셋의 월급이 250, 220. 230 일 때, 이번 달에 보너스로 월급의 2.1배를 지급하려 한다.
bonus_salary = np.array([250, 220, 230]) * 2.1
print(bonus_salary)

# mixed
# ndarray는 파이썬의 리스트 처럼 서로 다른 타입의 원소를 가질 수 없다.
# 다른 타입의 원소들이 섞여 있다면, 가장 우선 순위(byte)가 높은 타입으로 변환된다.
mixed = np.array([-9, 'daelim', False, 2.71])
print(mixed)

