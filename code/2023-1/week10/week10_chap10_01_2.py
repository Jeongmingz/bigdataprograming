# using property method

class VIPMember():
	def __init__(self, insert_name: str, tel: str, sex: bool):
		self.vipname = insert_name
		self.tel = tel
		self.sex = sex

	def get_name(self):
		print("Get VIP's name")
		return self.vipname

	def set_name(self, insert_name):
		print("Set VIP's name")
		self.vipname = insert_name

	# 이제 VIPMember Object는 name을 통해 getter, setter에 접근 할 수 있다.
	name = property(get_name, set_name)


door = VIPMember('moon', '01012341234', 0)
print(door.name)
door.set_name('moon J I')
print(door.name)  # property로 선언한 name을 이용한 호출은 설정해준 getter, setter를 거친다.
