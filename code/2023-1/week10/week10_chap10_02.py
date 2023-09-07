# using property Annotation

class VIPMember():
	def __init__(self, insert_name: str, tel: str, sex: bool):
		self.vipname = insert_name
		self.tel = tel
		self.sex = sex

	# 이전에 선언한 Method가 아닌 Annotation을 사용한 예시.
	# 기존의 get_name, set_name의 메소드 이름을 하나로 통일하고 (이 코드에선 name)
	# getter 부분에 property Annotation을 선언 하고 setter 부분엔 통일한 이름.setter로 선언.
	@property
	def name(self):
		print("Get VIP's name")
		return self.vipname

	@name.setter
	def name(self, insert_name):
		print("Set VIP's name")
		self.vipname = insert_name

	# getter만 property로 선언할 경우 readonly로 만들 수 있다.
	@property
	def tel(self):
		return self.tel


door = VIPMember('moon', '01012341234', 0)
print(door.name)
door.name = 'moon J I'
# door.set_name('moon J I')  # Annotation으로 선언 할 경우, setter, getter로 접근 할 수 없다.
print(door.name)  # property로 선언한 name을 이용한 호출은 설정해준 getter, setter를 거친다.
