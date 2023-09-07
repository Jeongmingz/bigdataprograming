# lambda

def squares(n):
    return n * n


# numbers = [squares(i) for i in range(10)]
numbers = [i for i in range(10)]

ss = list(map(squares, numbers))
ss2 = list(map(lambda x: x ** 2, numbers))

print(ss)
print(ss2)
