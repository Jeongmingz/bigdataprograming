import numpy as np
import tkinter as tk  # Built in GUI


def create_2darray(row, col):
	return np.random.randint(1, 101, size=(row, col))


def click_button(*args):
	n, m = map(int, en_number.get().split(' '))
	v = create_2darray(n, m)
	print(v)
	lbl_result.config(text=v)


window = tk.Tk()
window.title('numpy gui version v2.0')
window.geometry('300x150')


# create widget
lbl_result = tk.Label(text="random numpy array")
en_number = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button,)
en_number.bind("<Return>", click_button)
en_number.focus()


# widget layout
lbl_result.grid(row=0, column=0, columnspan=2)
en_number.grid(row=1, column=0,  columnspan=2, sticky=tk.EW)
btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

window.mainloop()
# n = int(input("input number : "))
# l = [random.randint(1, 100) for i in range(n)]
# v = np.array(l, dtype='int16')
# print(v)
