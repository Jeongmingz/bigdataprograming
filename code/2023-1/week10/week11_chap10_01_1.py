class Person:
	def __init__(self, name):
		self.hidden_name = name

	def get_name(self):
		return self.hidden_name

	def set_name(self, input_name):
		self.hidden_name = input_name


p = Person('이정민')
