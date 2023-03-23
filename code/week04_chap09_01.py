# def do_notting():
#     pass
#
# a = [1, 3, 5]
#
# print(a.pop())
# print(do_notting())

import tkinter as tk #built-in GUI

def factorial():
    '''
    안녕하세요안녕하세요
    :return: int
    '''
    n = int(en_number.get())
    result = 1
    for i in range(2, n+1):
        result = result * i
    lbl_factorial.config(text=f'{n}! = {result}') # 레이블에 결과 출력

win = tk.Tk()

win.title('chap09 function')
win.geometry('300x150')

lbl_factorial = tk.Label(text='팩토리얼 계산 프로그램')
en_number = tk.Entry() # 숫자 입력
btn_calculate = tk.Button(text='계산', command=factorial) # 순서는 상관 없다

# 배치 (pack, grid, place)
lbl_factorial.pack()
en_number.pack()
btn_calculate.pack(fill='x', )

win.mainloop()
