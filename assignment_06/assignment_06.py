# Assignment 6:
# Module 10 & 11: CALCULATOR USING TKINTER

from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x245")
window.resizable(False, False)

is_last_button_equals = False

# text box
tb = Entry(window, width=45, justify="right", borderwidth=3)
tb.place(x=10, y=10)

'''
Function definitions
'''
def click(number):
    global is_last_button_equals
    if is_last_button_equals:
        tb.delete(0, END)
        is_last_button_equals = False

    current = tb.get()
    tb.delete(0, END)
    tb.insert(0, str(current) + str(number))

def cleanup():
    tb.delete(0, END)

def add():
    current = tb.get()
    global operation
    operation = "addition"
    global num1
    num1 = int(current)
    tb.delete(0, END)

def subtract():
    current = tb.get()
    global operation
    operation = "subtraction"
    global num1
    num1 = int(current)
    tb.delete(0, END)

def multiply():
    current = tb.get()
    global operation
    operation = "multiplication"
    global num1
    num1 = int(current)
    tb.delete(0, END)

def divide():
    current = tb.get()
    global operation
    operation = "division"
    global num1
    num1 = int(current)
    tb.delete(0, END)

def equal():
    current = int(tb.get())
    tb.delete(0, END)
    if operation == "addition":
        tb.insert(0, num1 + current)
    elif operation == "subtraction":
        tb.insert(0, num1 - current)
    elif operation == "multiplication":
        tb.insert(0, num1 * current)
    elif operation == "division":
        try:
            tb.insert(0, num1 / current)
        except ZeroDivisionError:
            tb.insert(0, 'ERR: division by zero')

    global is_last_button_equals
    is_last_button_equals = True

'''
Button configurations
'''
number_button = Button(window, text = '1', width = 8, height= 2, borderwidth = 2, command=lambda: click(1))
number_button.place(x=10, y=40)

number_button = Button(window, text = '2', width = 8, height= 2, borderwidth = 2, command=lambda: click(2))
number_button.place(x=80, y=40)

number_button = Button(window, text = '3', width = 8, height= 2, borderwidth = 2, command=lambda: click(3))
number_button.place(x=150, y=40)

number_button = Button(window, text = '/', width = 8, height= 2, borderwidth = 2, command=divide)
number_button.place(x=220, y=40)

number_button = Button(window, text = '4', width = 8, height= 2, borderwidth = 2, command=lambda: click(4))
number_button.place(x=10, y=90)

number_button = Button(window, text = '5', width = 8, height= 2, borderwidth = 2, command=lambda: click(5))
number_button.place(x=80, y=90)

number_button = Button(window, text = '6', width = 8, height= 2, borderwidth = 2, command=lambda: click(6))
number_button.place(x=150, y=90)

number_button = Button(window, text = '*', width = 8, height= 2, borderwidth = 2, command=multiply)
number_button.place(x=220, y=90)

number_button = Button(window, text = '7', width = 8, height= 2, borderwidth = 2, command=lambda: click(7))
number_button.place(x=10, y=140)

number_button = Button(window, text = '8', width = 8, height= 2, borderwidth = 2, command=lambda: click(8))
number_button.place(x=80, y=140)

number_button = Button(window, text = '9', width = 8, height= 2, borderwidth = 2, command=lambda: click(9))
number_button.place(x=150, y=140)

number_button = Button(window, text = '-', width = 8, height= 2, borderwidth = 2, command=subtract)
number_button.place(x=220, y=140)

number_button = Button(window, text = 'C', width = 8, height= 2, borderwidth = 2, command=cleanup)
number_button.place(x=10, y=190)

number_button = Button(window, text = '0', width = 8, height= 2, borderwidth = 2, command=lambda: click(0))
number_button.place(x=80, y=190)

number_button = Button(window, text = '=', width = 8, height= 2, borderwidth = 2, command=equal)
number_button.place(x=150, y=190)

number_button = Button(window, text = '+', width = 8, height= 2, borderwidth = 2, command=add)
number_button.place(x=220, y=190)

'''
Main loop
'''
mainloop()


