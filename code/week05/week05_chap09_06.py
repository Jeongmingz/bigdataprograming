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

# 이미 ranger가 generator의 역할을 하고 한번 실행 이후 사라졌기 때문에
# 이번 for문은 실행하지 않는다.
for i in ranger:
    print(i, end=' ')
