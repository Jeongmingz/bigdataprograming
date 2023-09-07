import my_utility


def Fibonacci_recursion(n):
    """
    using recursion function, fibonacci number return
    :param n: input number
    :return: fibonacci number
    """
    if n == 0 or n == 1:
        return n
    else:
        return Fibonacci_recursion(n - 2) + Fibonacci_recursion(n - 1)


def fibonacci_repetition(n):
    """
    using repetition function 'for' , fibonacci number return
    :param n: input number
    :return: fibonacci number
    """
    if n == 0 or n == 1:
        return n
    else:
        result, t1, t2 = 1, 1, 0
        for i in range(2, n + 1):
            result = t1 + t2
            t2 = t1
            t1 = result
    return result


memo = {0: 0, 1: 1}  # 한번 수행한 피보나치 수를 저장.


def fibonacci_memoization(n):
    """
    using Dynamic Programing, fibonacci number return
    :param n: input number
    :return: fibonacci number
    """
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memoization(n-2) + fibonacci_memoization(n-1)
    return memo[n]


frep = my_utility.time_check(fibonacci_repetition)
frec = my_utility.time_check(Fibonacci_recursion)
fmemo = my_utility.time_check(fibonacci_memoization)
print(frep(100))
print(frec(30))
print(fmemo(100))
