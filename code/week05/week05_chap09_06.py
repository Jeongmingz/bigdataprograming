# generators

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        # yield는 함수를 종료하지 않고 만들어질 때 마다 보낸다
        yield number
        number += step


print(my_range())

ranger = my_range()

for i in ranger:
    print(i, end=' ')
