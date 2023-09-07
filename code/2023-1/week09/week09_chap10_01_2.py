class Animal:
	def say(self):
		return 'I am a animal'


class Dog(Animal):
	def say(self):
		return 'I am a dog'


class Cat(Animal):
	def say(self):
		return 'I am a cat'


class Dat(Dog, Cat):
	pass


class Cog(Cat, Dog):
	pass


cg = Cog()
gc = Dat()
print(cg.say())  # Method의 우선순위는 상속받는 첫번째 class의 Method를 사용한다. -> Dog
print(gc.say())  # Method의 우선순위는 상속받는 첫번째 class의 Method를 사용한다. -> Cat
print(Cog.mro())  # 차상위 계층의 class는 object다.
