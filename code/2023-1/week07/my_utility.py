# my_utility.py
import time


def time_check(func):  # closure
    def inner(*args, **kwargs):
        print(f"function name : {func.__name__}")
        print(f"function doc : {func.__doc__}")
        s = time.time()
        r = func(*args, **kwargs)
        e = time.time()
        print(f"함수를 처리하는데 걸린 시간 : {e - s}")
        return r

    return inner
