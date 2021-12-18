from tkinter import *
import parser
root = Tk()
root.title("Calculator")
root.geometry('400x224')

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)

Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)

Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)

Grid.rowconfigure(root, 4, weight=1)
Grid.columnconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)

i = 0


def get_variable(num):
    global i
    display.insert(i, num)
    i += 1


def get_operator(opt):
    global i
    lenght = len(opt)
    display.insert(i, opt)
    i += lenght


def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "error")


def calculate():
    entire_string = display.get()
    try:
        r = parser.expr(entire_string).compile()
        result = eval(r)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "error")


display = Entry(root, width=66)
display.grid(row=0, columnspan=5)

Button(root, text="AC", height=2, width=10, command=lambda: clear_all()).grid(row=1, column=0)
Button(root, text="Cr", height=2, width=10, command=lambda: undo()).grid(row=1, column=1)
Button(root, text="x^2", height=2, width=10, command=lambda: get_operator('**2')).grid(row=1, column=2)
Button(root, text="+", height=2, width=10, command=lambda: get_operator('+')).grid(row=1, column=3)
Button(root, text="pi", height=2, width=10, command=lambda: get_operator('3.14')).grid(row=1, column=4)

Button(root, text="7", height=2, width=10, command=lambda: get_variable(7)).grid(row=2, column=0)
Button(root, text="8", height=2, width=10, command=lambda: get_variable(8)).grid(row=2, column=1)
Button(root, text="9", height=2, width=10, command=lambda: get_variable(9)).grid(row=2, column=2)
Button(root, text="-", height=2, width=10, command=lambda: get_operator('-')).grid(row=2, column=3)
Button(root, text="(", height=2, width=10, command=lambda: get_operator('(')).grid(row=2, column=4)

Button(root, text="4", height=2, width=10, command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5", height=2, width=10, command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6", height=2, width=10, command=lambda: get_variable(6)).grid(row=3, column=2)
Button(root, text="*", height=2, width=10, command=lambda: get_operator('*')).grid(row=3, column=3)
Button(root, text=")", height=2, width=10, command=lambda: get_operator(')')).grid(row=3, column=4)

Button(root, text="1", height=2, width=10, command=lambda: get_variable(1)).grid(row=4, column=0)
Button(root, text="2", height=2, width=10, command=lambda: get_variable(2)).grid(row=4, column=1)
Button(root, text="3", height=2, width=10, command=lambda: get_variable(3)).grid(row=4, column=2)
Button(root, text="/", height=2, width=10, command=lambda: get_operator('/')).grid(row=4, column=3)
Button(root, text="exp", height=2, width=10, command=lambda: get_operator('**')).grid(row=4, column=4)

Button(root, text=".", height=2, width=10, command=lambda: get_operator('.')).grid(row=5, column=0)
Button(root, text="0", height=2, width=10, command=lambda: get_variable(0)).grid(row=5, column=1)
Button(root, text="=", height=2, width=10, command=lambda: calculate()).grid(row=5, column=2)
Button(root, text="%", height=2, width=10, command=lambda: get_operator('%')).grid(row=5, column=3)
Button(root, text="x!", height=2, width=10, command=lambda: get_operator('=!')).grid(row=5, column=4)

root.mainloop()
