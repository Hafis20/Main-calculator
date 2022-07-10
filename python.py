
from tkinter import *


window = Tk()
window.geometry('320x530')
window.configure(bg='blue')


def click(num):
    first_number = txt_here.get()
    txt_here.delete(0, END)
    txt_here.insert(0, str(first_number)+str(num))


def add():
    first_number = txt_here.get()
    global old_number
    old_number = float(first_number)
    global math
    math ='Addition'
    txt_here.delete(0,END)


def minus():
    first_number = txt_here.get()
    global old_number
    old_number = float(first_number)
    global math
    math = 'subtraction'
    txt_here.delete(0, END)


def mul():
    first_number = txt_here.get()
    global old_number
    old_number = float(first_number)
    global math
    math = 'multiplication'
    txt_here.delete(0,END)


def div():
    first_number = txt_here.get()
    global old_number
    old_number = float(first_number)
    global math
    math = 'division'
    txt_here.delete(0,  END)


def equal():

    if math == 'Addition':
        new_number = txt_here.get()
        txt_here.delete(0, END)
        txt_here.insert(0, str(float(old_number)+float(new_number)))

    if math == 'subtraction':
        new_number = txt_here.get()
        txt_here.delete(0, END)
        txt_here.insert(0, str(float(old_number)-float(new_number)))

    if math == 'multiplication':
        new_number = txt_here.get()
        txt_here.delete(0, END)
        txt_here.insert(0, str(float(old_number)*(float(new_number))))

    if math == 'division':
        new_number = txt_here.get()
        txt_here.delete(0, END)
        txt_here.insert(0, str(float(old_number)/float(new_number)))


def clear():
    txt_here.delete(0, END)

txt_here = Entry(window, justify=RIGHT, bg='grey')
txt_here.grid(row=0, column=0, columnspan=30, ipady=29, ipadx=72)


seven_button = Button(window, text='7', width=5, height=4, bg='yellow', command=lambda: click(7))
seven_button.grid(row=2, column=0, padx=5, pady=5)
eight_button = Button(window, text='8', width=5, height=4, bg='yellow', command=lambda: click(8))
eight_button.grid(row=2, column=1, padx=5, pady=5)
nine_button = Button(window, text='9', width=5, height=4, bg='yellow', command=lambda: click(9))
nine_button.grid(row=2, column=2, padx=5, pady=5)
four_button = Button(window, text='4', width=5, height=4, bg='yellow', command=lambda: click(4))
four_button.grid(row=3, column=0, padx=5, pady=5)
five_button = Button(window, text='5', width=5, height=4, bg='yellow', command=lambda:  click(5))
five_button.grid(row=3, column=1, padx=5, pady=5)
six_button = Button(window, text='6',  width=5, height=4, bg='yellow', command=lambda: click(6))
six_button.grid(row=3, column=2, padx=5, pady=5)
one_button = Button(window, text='1', width=5, height=4, bg='yellow', command=lambda: click(1))
one_button.grid(row=4, column=0, padx=5, pady=5)
two_button = Button(window,text='2',  width=5, height=4, bg='yellow',command=lambda: click(2))
two_button.grid(row=4, column=1, padx=5, pady=5)
three_button = Button(window,  text='3',  width=5, height=4, bg='yellow',command=lambda: click(3))
three_button.grid(row=4, column=2, padx=5, pady=5)
zero_button = Button(window, text='0', width=5, height=4, bg='yellow',command=lambda: click(0))
zero_button.grid(row=5, column=0,padx=5, pady=5)
dot_button = Button(window, text='.', width=5, height=4, bg='yellow',command=lambda: click('.'))
dot_button.grid(row=5, column=1, padx=5, pady=5)

#operation_buttons
clear_button = Button(window, text='clear', width=5, height=4, bg='green', command=clear)
clear_button.grid(row=5, column=2, padx=5, pady=5)
div_button = Button(window, text='/', width=5, height=4, bg='green', command=div)
div_button.grid(row=2, column=4, padx=5, pady=5)
mul_button = Button(window, text='x', width=5, height=4, bg='green', command=mul)
mul_button.grid(row=3, column=4, padx=5, pady=5)
minus_button = Button(window, text='-', width=5, height=4, bg='green', command=minus)
minus_button.grid(row=4, column=4, padx=5, pady=5)
plus_button = Button(window, text='+', width=5, height=4, bg='green', command=add)
plus_button.grid(row=5, column=4, padx=5, pady=5)
equal_button = Button(window, text='=', width=35, height=3, bg='green', command=equal)
equal_button.grid(row=6, column=0, padx=5, pady=5,columnspan=5)
window.mainloop()

