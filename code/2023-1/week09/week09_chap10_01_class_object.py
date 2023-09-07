import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius


class Cylinder(Circle):
    def __init__(self, height, radius):
        # self.radius = radius
        super().__init__(radius)
        self.height = height

    def get_volumn(self) -> float:
        return math.pi * self.radius * self.radius * self.height


class Bool(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def get_volumn(self) -> float:
        return math.pi * self.radius * self.radius * self.radius * self.radius


c1 = Circle(10)
print(c1.get_area())


cy1 = Cylinder(100, 10)
print(cy1.get_volumn())


b1 = Bool(10)
print(b1.get_volumn())
