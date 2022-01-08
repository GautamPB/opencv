from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(background = "blue")
root.geometry("250x250")
pic = PhotoImage(file = "calculator-icon.png")
root.iconphoto(False, pic)

def clear_screen():
    txt.delete(0.0, 'end')

def write_one():
    txt.insert('end', "1")

def write_two():
    txt.insert('end', "2")

def write_three():
    txt.insert('end', "3")

def write_four():
    txt.insert('end', "4")

def write_five():
    txt.insert('end', "5")

def write_six():
    txt.insert('end', "6")

def write_seven():
    txt.insert('end', "7")

def write_eight():
    txt.insert('end', "8")

def write_nine():
    txt.insert('end', "9")

def write_zero():
    txt.insert('end', "0")

def add():
    txt.insert('end', "+")

def subtract():
    txt.insert('end', "-")

def multiply():
    txt.insert('end', "x")

def divide():
    txt.insert('end', "/")

def calc():
    operations = ['+', '-', 'x', '/']
    data = txt.get(0.0, 'end')
    num1 = ""
    num2 = ""
    operation = ""
    found_operation = False
    for i in data:
        if(i in operations):
            found_operation = True
            operation = i
            continue
        if(found_operation == False):
            if(i.isdigit() == True):
                num1 += i
        else:
            if(i.isdigit() == True):
                num2 += i

    n1 = int(num1)
    n2 = int(num2)
    txt.delete(0.0, 'end')
    if (operation == "+"):
        ans = n1 + n2
        final = str(ans)
        txt.insert(0.0, final)

    elif (operation == "-"):
        ans = n1 - n2
        final = str(ans)
        txt.insert(0.0, final)

    elif (operation == "x"):
        ans = n1 * n2
        final = str(ans)
        txt.insert(0.0, final)

    elif (operation == "/"):
        ans = n1 / n2
        final = str(ans)
        txt.insert(0.0, final)

fm = Frame(root)
fm.pack()
txt = Text(fm, width = 18, height = 2, wrap = WORD, bg = "grey", fg = "black")
clear = Button(fm, text = "CLR", height = 2, width = 4, command = clear_screen, fg = "black", bg = "grey")
equals = Button(fm, text = "=", height = 2, width = 4, command = calc, bg = "grey", fg = "black")
plus = Button(fm, text = "+", height = 2, width = 4, command = add, fg = "white", bg = "red")
minus = Button(fm, text = "-", height =2, width = 4, command = subtract, fg = "white", bg = "red")
prod = Button(fm, text = "X", height = 2, width = 4, command = multiply, fg = "white", bg = "red")
div = Button(fm, text = "/", height = 2, width = 4, command = divide, fg = "white", bg = "red")
b1 = Button(fm, text = "1", height = 2, width = 4, command = write_one, bg = "black", fg = "white")
b2 = Button(fm, text = "2", height = 2, width = 4, command = write_two, bg = "black", fg = "white")
b3 = Button(fm, text = "3", height = 2, width = 4, command = write_three, bg = "black", fg = "white")
b4 = Button(fm, text = "4", height = 2, width = 4, command = write_four, bg = "black", fg = "white")
b5 = Button(fm, text = "5", height = 2, width = 4, command = write_five, bg = "black", fg = "white")
b6 = Button(fm, text = "6", height = 2, width = 4, command = write_six, bg = "black", fg = "white")
b7 = Button(fm, text = "7", height = 2, width = 4, command = write_seven, bg = "black", fg = "white")
b8 = Button(fm, text = "8", height = 2, width = 4, command = write_eight, bg = "black", fg = "white")
b9 = Button(fm, text = "9", height = 2, width = 4, command = write_nine, bg = "black", fg = "white")
b0 = Button(fm, text = "0", height = 2, width = 4, command = write_zero, bg = "black", fg = "white")

txt.grid(row = 0, columnspan = 4)
b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b0.grid(row = 4, column = 0)
clear.grid(row = 4, column = 2)
plus.grid(row = 1, column = 3)
minus.grid(row = 2, column = 3)
prod.grid(row = 3, column = 3)
div.grid(row = 4, column = 3)
equals.grid(row = 4, column = 1)

root.mainloop()