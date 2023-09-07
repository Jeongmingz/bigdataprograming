# week14_chap_visualization_06.py
import matplotlib.pyplot as plt
import numpy as np

# x (0 < x <20)

years = [1965, 1975, 1985, 1995, 2005, 2015]
korea = [130, 650, 2450, 11200, 17790, 27250]
japan = [890, 5120, 11500, 42130, 40560, 38780]
china = [100, 200, 290, 540, 1760, 7940]

# x_range = range(len(years))
x_range = np.arange(len(years))
plt.bar(x_range+0.0, korea, color='yellow', width=0.25)
plt.bar(x_range+0.3, japan, color='red', width=0.25)
plt.bar(x_range+0.6, china, color='blue', width=0.25)
plt.xticks(range(len(years)), years)

plt.show()
