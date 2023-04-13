def fibonacci(n):
    """
    using recursion function, fibonacci number return
    :param n: input number
    :return: fibonacci number
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


