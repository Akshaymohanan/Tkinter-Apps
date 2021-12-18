from tkinter import *
root = Tk()
root.title("NotePad")


def save():
    a = text.get("1.0", "end-1c")
    file1 = open("new.txt", "w")
    file1.write(a)
    file1.close()


def undo():
    global t
    a = text.get("1.0", "end-1c")
    t = a
    temp = a[:-1]
    text.delete("1.0", "end-1c")
    text.insert("0.0", temp)


def redo():
    text.delete("1.0", "end-1c")
    text.insert("0.0", t)


def cut():
    global cb
    a = text.get("1.0", "end-1c")
    cb = a
    text.delete("1.0", "end-1c")


def copy():
    global cb
    a = text.get("1.0", "end-1c")
    cb = a


def paste():
    text.insert(END, cb)


mymenu = Menu(root)
root.config(menu=mymenu)

submenu1 = Menu(mymenu)
submenu2 = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="Save", command=save)
submenu1.add_separator()
submenu1.add_command(label="Quit", command=root.quit)

mymenu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Undo", command=undo)
submenu2.add_command(label="Redo", command=redo)
submenu2.add_separator()
submenu2.add_command(label="Cut", command=cut)
submenu2.add_command(label="Copy", command=copy)
submenu2.add_command(label="Paste", command=paste)

text = Text(root)
text.pack()

root.mainloop()
