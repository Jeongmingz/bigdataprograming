class Pokemon:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('setter')
        self.hidden_name = input_name


p1 = Pokemon('피카츄')

print(p1.name)
p1.name = '라이츄'
print(p1.name)
