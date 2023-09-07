class VIPMember:
	def __init__(self, name: str, tel: str, sex: bool):
		self.name = name
		self.tel = tel
		self.sex = sex

	def get_name(self):
		print("Get VIP's name")
		return self.name

	def set_name(self, name):
		print("Set VIP's name")
		self.name = name


door = VIPMember('moon', '01012341234', 0)
print(door.get_name())
door.set_name('moon J I')
print(door.get_name())
print(door.name)  # getter 메소드를 사용하지 않고 name에 접근 했을 때, print("Get VIP's name")가 실행하지 않는다.
