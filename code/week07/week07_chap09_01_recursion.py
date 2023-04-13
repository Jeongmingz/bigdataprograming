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


frep = my_utility.time_check(fibonacci_repetition)
frec = my_utility.time_check(Fibonacci_recursion)
print(frep(100))
print(frec(30))
