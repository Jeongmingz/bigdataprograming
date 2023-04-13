# week06_chap09_01_closure_review.py
# closure

import time


def time_check(func):  # closure
	def inner(*args):
		print(f"function name : {func.__name__}")
		s = time.time()
		r = func(*args)
		e = time.time()
		print(f"함수를 처리하는데 걸린 시간 : {e - s}")
		return r

	return inner


@time_check
def do_something():
	total = 0
	print("함수에서 무언가 작업을 합니다.")
	for k in range(1, 1000000):
		total = total + k


@time_check
def factorial(n):
	result = 1
	for i in range(2, n + 1):
		result = result * i
	return result  # 레이블에 결과 출력


print(factorial(10))


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
