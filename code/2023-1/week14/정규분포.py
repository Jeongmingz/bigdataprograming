# week14_chap_visualization_06.py
import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(20, 50)
y_data = x_data + 2 * np.random.randn(30)  # 정규분포

plt.plot(y_data, y_data)
plt.scatter(x_data, y_data)

plt.title('Real age VS Physical age')
plt.xlabel('Real age')
plt.ylabel('Physical age')


plt.show()
