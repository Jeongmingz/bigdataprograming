class Animal:
    def says(self):
        return 'I speak!'

    def eating(self):
        return "I'm eating!!"


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


m1 = Mule()
print(m1.says())
print(m1.eating())
print(Mule.mro())
