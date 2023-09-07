# week11_chap10_01_aggregation.py
class Pokemon:
    pokemon_count = 0  # class variable

    def __init__(self, input_name, input_level):
        self.__name = input_name  # __name is like private access
        self.__level = input_level
        Pokemon.pokemon_count += 1

    def __str__(self):
        _return = {'type': type(self), 'id': id(self), 'name': self.__name, 'level': self.__level}
        return str(_return)

    def __add__(self, pokemon):
        """
        포켓몬들의 레벨의 합을  리턴하는 메직 메소드
        :param pokemon: + 연산기호 우측 Pokemon 객체
        :return: 두 객체의 레벨의 합
        """
        return self.__level + pokemon.__level

    @property
    def name(self):
        print('getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('setter')
        self.__name = input_name

    @property
    def level(self):
        print('getter')
        return self.__level

    @level.setter
    def level(self, input_level):
        print('setter')
        self.__level = input_level

    @classmethod
    def get_pokemon_count(cls):
        return cls.pokemon_count

    @staticmethod
    def info():
        print('포켓몬에 관련한 클래스입니다. ')


# aggregation
class Trainer:
    def __init__(self, pokemon, name):
        self.pokemon = pokemon
        self.name = name

    def pokemon_info(self):
        print(f'{self.name}의 소유 포켓몬은 {self.pokemon}입니다.\n'
              f'{self.pokemon.name}의 레벨은 {self.pokemon.level}')


Pokemon.info()

print(Pokemon.pokemon_count)

p1 = Pokemon('피카츄', 1)
p2 = Pokemon('리자몽', 36)

t1 = Trainer(p1, '한지우')

t1.pokemon_info()



# print(p1)
# print(p1 + p2)  # == print(p1.__add__(p2))

# Pokemon.pokemon_count = 9
# print(Pokemon.get_pokemon_count())
# p3 = Pokemon('이상해', 3)
# print(Pokemon.pokemon_count)
# print(p3.pokemon_count)
#
# print(p1.name)
# # p1.name = '라이츄'
# p1.__name = '라이츄'  # 변경시킬 수 없음.
# print(p1.name)
# # print(p1.__name)
# print(p1._Pokemon__name)  # 접근 할 수 있으니, real private는 아님. (_클래스명__name으로 접근 가능)