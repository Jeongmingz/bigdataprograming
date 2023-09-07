# week06_chap09_02_scope.py


# week06_chap09_02_scope.py

animal = "과일박쥐"


def print_animal():
	global animal
	plants = "장미"
	animal = '웜뱃'

	print(animal, id(animal))


print_animal()
print(animal, id(animal))
print(locals())


# def print_animal():
# 	animal = '웜뱃'
#
# 	print(animal, id(animal))
#
#
# print_animal()
# print(animal, id(animal))
