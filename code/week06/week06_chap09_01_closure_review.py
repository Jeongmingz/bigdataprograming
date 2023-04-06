# week06_chap09_01_closure_review.py
# closure

import time


def time_check(func):  # closure
	def inner(*args, **kwargs):
		print(f"function name : {func.__name__}")
		print(f"function doc : {func.__doc__}")
		s = time.time()
		r = func(*args, **kwargs)
		e = time.time()
		print(f"함수를 처리하는데 걸린 시간 : {e - s}")
		print(f"결과 : {r}")
		return r

	return inner

# Decorators 어노테이션
@time_check
def do_something():
	total = 0
	print("함수에서 무언가 작업을 합니다.")
	for k in range(1, 1000000):
		total = total + k


@time_check
def factorial(n):
	'''
	팩토리얼 함수 (for 문 사용)
	:param n:
	:return: Type: int , 팩토리얼 계산 결과 값.
	'''
	result = 1
	for i in range(2, n + 1):
		result = result * i
	return result  # 레이블에 결과 출력


# @time_check
def factorial_recursion(n):
	"""
	팩토리얼 함수 (recursion 재귀함수 사용)
	:param n: Type : int, 입력값
	:return: Type: int , 팩토리얼 계산 결과 값.
	"""

	if n == 1:
		return 1
	else:
		return n * factorial_recursion(n-1)

@time_check
def power(base, exponent):
	"""
	거듭제곱 함수, 내장 함수인 pow | ** 와 같은 결과
	:param base: 밑 Type:int
	:param exponent: 지수 Type:int
	:return: 거듭제곱 결과 값 Type:int
	"""
	result = 1
	for _ in range(exponent):
		result *= base

	return result


factorial(10)
print(factorial_recursion(10))
power(exponent=4, base=2)


# daelim_func = time_check(factorial)
# daelim_func()

# 매 함수마다 시간을 재는 코드를 넣는 것은 비 효율적
# import time
#
# def do_something():
# 	s = time.time()
# 	total = 0
# 	print("함수에서 무언가 작업을 합니다.")
# 	for k in range(1,1000000):
# 		total = total + k
# 	e = time.time()
# 	print(f"함수를 처리하는데 걸린 시간 : {e-s}")
#
# do_something()
