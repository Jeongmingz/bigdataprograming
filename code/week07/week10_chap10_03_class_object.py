# week07_chap10_03_class_object.py

class Cat:
    pass


a_cat = Cat()
another_cat = Cat()

print(type(a_cat), id(a_cat))
print(type(another_cat),  id(another_cat))

a_cat.age = 3
a_cat.name = "냥"
a_cat.nemesis = another_cat

print(a_cat.age, a_cat.name, a_cat.nemesis)
another_cat.name = "냥냥"
print(a_cat.nemesis.name)
