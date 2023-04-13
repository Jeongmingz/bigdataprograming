# week07_chap10_03_class_object.py
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#
# cat1 = Cat('봉다리')
# cat2 = Cat('포도')

class Car:
    def __init__(self, kind):
        self.kind = kind

    def exclaim(self):
        print('I am a car')


class Hyundai(Car):
    def __init__(self, kind, level):
        super().__init__(kind)  # 부모 클래스 필드 사용
        self.level = level  # 자식 클래스 자체 필드 사용

    def exclaim(self):
        print('I am a Hyundai car')

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car('화물차')
give_me_a_hyundai = Hyundai('승용차', '중형차')

print(give_me_a_car.kind)
print(give_me_a_hyundai.kind, give_me_a_hyundai.level)

give_me_a_hyundai.exclaim()
give_me_a_car.exclaim()

print(issubclass(Hyundai, Car))
