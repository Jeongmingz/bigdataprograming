class Kartrider:
	kartrider_player_cnt = 0

	def __init__(self, input_name, input_level):
		self.__player_name = input_name
		self.__player_level = input_level
		Kartrider.kartrider_player_cnt += 1

	def __str__(self):
		_return = {'class': self.__class__, 'player_name': self.__player_name, 'player_level': self.__player_level}
		return str(_return)

	def __add__(self, kartrider):
		return self.__player_level + kartrider.__player_level

	@property
	def name(self):
		return self.__player_name

	@name.setter
	def name(self, input_name):
		self.__player_name = input_name

	@property
	def level(self):
		return self.__player_level

	@level.setter
	def level(self, input_level):
		self.__player_level = input_level

	def level_up(self, up_scale):
		self.__player_level += up_scale

	# class의 member 변수를 접근 할 수 있게 된다.
	@classmethod
	def get_kartrider_player_cnt(cls):
		return cls.kartrider_player_cnt

	# static method 생성 : class object생성 전에도 사용 가능한 메소드가 된다. => ClassName.info() 이런식으로
	@staticmethod
	def info():
		print('카트라이더 복귀 기원 1일차')


Kartrider.info()

print(Kartrider.get_kartrider_player_cnt())
jeong = Kartrider('Lee Jeong Min', 32)
ji = Kartrider('Kim Ji Hyun', 61)
print(Kartrider.get_kartrider_player_cnt())

print(jeong.__str__())
print(jeong)

print(ji.__str__())

print(jeong + ji)

