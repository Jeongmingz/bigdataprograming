numbers = input("두수를 입력해주세요. (스페이스로 분리)").split()
list_ = []

for i in range(int(numbers[0]), int(numbers[1]) + 1):
    list_.append(i)

print(list_)

blurt = "What the..?.!!?"

print(blurt.strip('.!?'))
