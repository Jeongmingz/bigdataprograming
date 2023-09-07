# week14_chap_visualization_03.py
import matplotlib.pyplot as plt
import numpy as np

# y = 2x
# y = x**2 + 5
# y = -x**2 - 5

# x (-20 < x <20)

x = np.arange(-20,20)
y = x * 2
print(y)
plt.plot(x, y, color='black')

y = x ** 2 + 5
plt.plot(x, y, color='blue')

y = -x ** 2 - 5
plt.plot(x, y, 'r-')


plt.axis([-200, 200, -400, 400])
plt.show()
