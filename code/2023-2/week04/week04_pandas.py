import pandas as pd
from sklearn.linear_model import LinearRegression

# Download and prepare the data
life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")

X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d Array
y = life_satisfaction[["Life satisfaction"]].values


# Visualize the data
import matplotlib.pyplot as plt

life_satisfaction.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23500, 62500, 4, 9])
plt.show()

# model choice
model = LinearRegression()

# model train
model.fit(X, y)

# predict new GDP per capita Cyprus 2020
X_new = [[31700]]  # Cyprus' GDP per capita in 2020
print(life_satisfaction)
print(model.predict(X_new))  # outputs [[6.30165767]]
