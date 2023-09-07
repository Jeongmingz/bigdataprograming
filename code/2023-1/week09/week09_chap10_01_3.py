class Pokemon:
	def __init__(self, name, hp, level, dmg, speed):
		self.name = name
		self.hp = hp
		self.level = level
		self.dmg = dmg
		self.speed = speed

	def attack(self):
		return f'{self.name}이(가) {self.dmg}의 데미지로 공격했습니다!'

	def escape(self):
		import random
		num = random.randrange(0, 100)
		if num <= self.speed:
			return f'{num}:{self.speed} {self.name}이(가) 도망쳤다!'
		else:
			return f'{num}:{self.speed} 도망치지 못했다.'

	def skill(self):
		import pokemon_lib as lib
		lib.skill()


p = Pokemon('피카츄', 100, 2, 3, 7)
print(p.attack())
print(p.escape())
p.skill()
