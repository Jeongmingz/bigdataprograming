# is_prime function

def is_prime(n):
    """
    Return True or False whether the argument is prime number or not
    :param n: input integer value
    :return: bool (if n is prime number then return Ture)
    """
    if i <= 1:
        return False
    else:
        for k in range(2, i):
            if i % k == 0:
                return False
    return True


# if start > end:
#     start, end = end, start

start, end = sorted(map(int, input().split()))

for i in range(start, end+1):
    if is_prime(i):
        print(i, end=' ')