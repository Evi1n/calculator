from tkinter import *

# Window settings
calculator = Tk()
calculator.resizable(width=False, height=False)
calculator.title("Calculator by Eviln")

# Entry settings
ent = Entry(calculator, borderwidth=2, width=50, bg="#8ca6ff")
ent.grid(row=0, column=0, columnspan=4)

# Define to the functions
def click(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))
    
def clear():
        ent.delete(0, END)

def add():
    first_number = ent.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    ent.delete(0, END)

def subtraction():
    first_number = ent.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    ent.delete(0, END)

def multiplication():
    first_number = ent.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    ent.delete(0, END)

def divide():
    first_number = ent.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    ent.delete(0, END)

def mod():
    first_number = ent.get()
    global f_num
    global math
    math = "mod"
    f_num = int(first_number)
    ent.delete(0, END)

def equal():
    second_number = ent.get()
    ent.delete(0, END)
    if math=="addition":
        ent.insert(0, f_num + int(second_number))
    if math=="multiplication":
        ent.insert(0, f_num * int(second_number))
    if math=="subtraction":
        ent.insert(0, f_num - int(second_number))
    if math=="division":
        ent.insert(0, f_num / int(second_number))
    if math=="mod":
        ent.insert(0, f_num % int(second_number))


# Define Buttons
# row 1 buttons
button_add = Button(calculator, text="+", padx=30, pady=30,bg="#d14c79", command=add)
button_sub = Button(calculator, text="-", padx=30, pady=30, bg="#d14c79", command=subtraction)
button_mult = Button(calculator, text="*", padx=30, pady=30, bg="#d14c79", command=multiplication)
button_empty = Button(calculator, text="  ", padx=30.5, pady=30, bg="pink")

# row 2 buttons
button_1 = Button(calculator, text="1", padx=30, pady=30,bg="pink", command=lambda:click(1))
button_2 = Button(calculator, text="2", padx=30, pady=30,bg="pink", command=lambda:click(2))
button_3 = Button(calculator, text="3", padx=30, pady=30,bg="pink", command=lambda:click(3))
button_div = Button(calculator, text="/", padx=31, pady=30,bg="#d14c79", command=divide)

# row 3 buttons
button_4 = Button(calculator, text="4", padx=30, pady=30,bg="pink", command=lambda:click(4))
button_5 = Button(calculator, text="5", padx=30, pady=30,bg="pink", command=lambda:click(5))
button_6 = Button(calculator, text="6", padx=30, pady=30,bg="pink", command=lambda:click(6))
button_mod = Button(calculator, text="%", padx=30, pady=30, bg="#d14c79", command=mod)

# row 4 buttons
button_7 = Button(calculator, text="7", padx=30, pady=30,bg="pink", command=lambda:click(7))
button_8 = Button(calculator, text="8", padx=30, pady=30,bg="pink", command=lambda:click(8))
button_9 = Button(calculator, text="9", padx=30, pady=30,bg="pink", command=lambda:click(9))
button_equal = Button(calculator, text="=", padx=30, pady=30, bg="#d14c79", command=equal)

# row 5 buttons
button_empty2 = Button(calculator, text="  ", bg="pink", padx=30, pady=30)
button_0 = Button(calculator, text="0", padx=30, pady=30,bg="pink", command=lambda:click(0))
button_empty3 = Button(calculator, text="  ", padx=30, pady=30, bg="pink")
button_clear = Button(calculator, text="Clear", padx=21, pady=30, bg="#8ca6ff", command=clear)


# Put the buttons on the screen
# row 1
button_add.grid(row=1, column=0)
button_sub.grid(row=1, column=1)
button_mult.grid(row=1, column=2)
button_empty.grid(row=1, column=3)

# row 2
button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_div.grid(row=2, column=3)

# row 3
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_mod.grid(row=3, column=3)

# row 4
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

# row 5
button_empty2.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_empty3.grid(row=5, column=2)
button_clear.grid(row=5, column=3)

calculator.mainloop()