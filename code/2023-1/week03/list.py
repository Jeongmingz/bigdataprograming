from copy import deepcopy
a = [['ace', 9], 2, 3]
b = a.copy()
c = list(a)
d = a[:]
e = a
f = deepcopy(a)

print(a, b, c, d, e, f)
print(id(a), id(b), id(c), id(d), id(e), id(f))

a[0][1] = 'CPP 어려워'
print(a, b, c, d, e, f)
