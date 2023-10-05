import pandas as pd
import tkinter as tk
from userLib.jmlearn import LinearRegression


def predict_life_satisfaction():
	X_new = [[int(en_GDP_per_capita.get())]]

	# Download and prepare the data
	life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
	X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d Array
	y = life_satisfaction[["Life satisfaction"]].values

	# Visualize the data
	# import matplotlib.pyplot as plt
	#
	# life_satisfaction.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
	# plt.axis([23500, 62500, 4, 9])
	# plt.show()

	# model choice
	model = LinearRegression()

	# model train
	model.fit(X, y)

	# predict new GDP per capita Cyprus 2020
	# X_new = [[31700]]  # Cyprus' GDP per capita in 2020
	# print(life_satisfaction)
	# print(model.predict(X_new))  # outputs [[6.30165767]]

	lbl_life_satisfaction.config(text=f'해당 국가의 삶의 만족도는 {model.predict(X_new)}')


if __name__ == "__main__":
	window = tk.Tk()
	window.title("삶의 만족도 예측 프로그램")
	window.geometry("300x150")

	lbl_life_satisfaction = tk.Label(text="삶의 만족도")
	en_GDP_per_capita = tk.Entry(window)
	btn_predict = tk.Button(window, text="에측하기", command=predict_life_satisfaction)

	lbl_life_satisfaction.pack()
	en_GDP_per_capita.pack(fill='x')
	btn_predict.pack(fill='x')

	window.mainloop()

