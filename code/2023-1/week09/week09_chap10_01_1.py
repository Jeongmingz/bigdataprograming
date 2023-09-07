class Square:
	def __init__(self, width):
		self.width = width

	def get_area(self):
		return pow(self.width, 2)


class Rectangle(Square):
	def __init__(self, height, width):
		super().__init__(width)
		self.height = height

	def get_area(self):
		return self.width * self.height


class Cube(Square):
	def __init__(self, width):
		super().__init__(width)

	def get_volumn(self):
		return pow(self.width, 3)

s = Square(10)
print(s.get_area())

r = Rectangle(10, 20)
print(r.get_area())

c = Cube(10)
print(c.get_volumn())
print(c.get_area())