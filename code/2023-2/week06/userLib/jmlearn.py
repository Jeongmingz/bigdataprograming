import numpy as np


class LinearRegression:
	def __init__(self):
		self.slope = None
		self.intercept = None

	def fit(self, X, y) -> None:
		"""
		Modeling Function
		:param X: Independent Variable (2d Array format)
		:param y: Dependent Variable (2d Array format)
		:return: None
		"""
		X_mean = np.mean(X)
		y_mean = np.mean(y)

		denominator = np.sum(pow((X - X_mean), 2))
		numerator = np.sum((X - X_mean) * (y - y_mean))

		self.slope = numerator / denominator
		self.intercept = y_mean - (self.slope * X_mean)

	def predict(self, X) -> list:
		"""
		Predict Value for input
		:param X: New Independent Variable (Single Value)
		:return: Predict Value for input (2d format)
		"""
		return self.slope * np.array(X) + self.intercept
