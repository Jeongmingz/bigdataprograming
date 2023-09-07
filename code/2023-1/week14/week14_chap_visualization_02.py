# week14_chap_visualization_02.py
import matplotlib.pyplot as plt

# y = 2x
# x (-10 < x < 10)

x = [x for x in range(-10, 10)]
y = [x*2 for x in x]

plt.plot(x, y)
plt.axis([-20, 20, -20, 20])
plt.show()
