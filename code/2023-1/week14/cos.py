# cos.py
import matplotlib.pyplot as plt
import numpy as np
import math

# x (0 < x <20)

x = np.arange(360)
y = list()

for angle in x:
	y.append(math.cos(math.radians(angle)))

plt.plot(x, y)
plt.title('cos wave')
plt.show()
