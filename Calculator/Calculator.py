# This is the code to make an easy calculator that adds, multiplies, subtracts and divide.

import tkinter   # Import tkinter
from tkinter import * # Import everything from tkinter
from functools import partial # Importing partial from functools

# Starting wiht gui 
win = Tk(className='Calculator') 

# Defining variables and functions of the calculator
def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='The sum is:%d' %sum)

def multiply(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    multiply = int(n1) * int(n2)
    label.config(text='The product is:%d' %multiply)

def subtract(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    subtract = int(n1) - int(n2)
    label.config(text='The subtraction is:%d' %subtract)

def divide(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    divide = int(n1) / int(n2)
    label.config(text='The division is:%d' %divide)

# Designing the GUI  

l1 = Label(win, text='First Number:' )
l1.grid(row=1, column=0)
l2 = Label(win, text='Second Number:')
l2.grid(row=2, column=0)
label = Label(win)
label.grid(row=6, column=4)
x1 = StringVar()
x2 = StringVar()
e1 = Entry(win, textvariable=x1)
e1.grid(row=1, column=2)
e2 = Entry(win, textvariable=x2)
e2.grid(row=2, column=2)
sum = partial(sum, label,x1,x2)
multiply = partial(multiply, label,x1,x2)
subtract = partial(subtract, label,x1,x2)
divide = partial(divide, label,x1,x2)
button = Button(win, text = "Add", command=sum, activeforeground='red', fg='blue')
button.grid(row=3, column=0)
button_2 = Button(win, text = "Multiply", command=multiply, activeforeground='red', fg='blue')
button_2.grid(row=3, column=1)
button_3 = Button(win, text = "Subtract", command=subtract, activeforeground='red', fg='blue')
button_3.grid(row=3, column=2)
button_4 = Button(win, text = "Divide", command=divide, activeforeground='red', fg='blue')
button_4.grid(row=3, column=3)
win.mainloop()