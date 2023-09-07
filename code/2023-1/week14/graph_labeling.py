# week14_chap_visualization_03.py
import matplotlib.pyplot as plt
import numpy as np

# x (0 < x <20)

x = np.arange(0,20)
y = x ** 2
z = x ** 3
c = 2 ** x
print(c)
plt.plot(x, x, color='black', label='linear')
plt.plot(x, y, color='blue', label='quadratic')
plt.plot(x, z, 'r-', label='qubic')
plt.plot(x, c, 'y-', label='h')

plt.legend()
plt.title('graph')

plt.show()
