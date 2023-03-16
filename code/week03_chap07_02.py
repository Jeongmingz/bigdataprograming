cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I wont eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:  # for문이 정상적으로 종료되었을 때 실행되는 else문
    print("Didn't find anything that started with 'x'")
