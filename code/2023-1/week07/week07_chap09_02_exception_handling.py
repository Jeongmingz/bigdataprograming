# week07_chap09_02_exception_handling.py
try:
    F: float = float(input("화씨 온도를 입력해보세요 >> "))
    C: float = (F-32) * 5/9
    print(f"화씨 {F}도는 섭씨 {C:.3f}도 입니다.")

    # raise "예외를 강제로 던진다 ㅋ"
    raise Exception('내가 던지는 예외이다') # C++, JAVA => throw,s
except IndexError as err:
    pass
except ZeroDivisionError as err:
    pass
except ValueError as err:
    print(err)
    print('입력 값을 확인하세요. 입력 값은 수치형이여야 합니다.')
except Exception as other:
    print(other)
    print("에러가 발생했다.")


