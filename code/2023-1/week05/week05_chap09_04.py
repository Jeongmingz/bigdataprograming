# Inner Functions
# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)

# print(outer(4, 7))

# closure

def outer(a, b):
    def inner():
        return a + b
    return inner

print(outer(1,3))