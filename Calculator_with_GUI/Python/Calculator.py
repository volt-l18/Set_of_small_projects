from tkinter import *
from tkinter import ttk

input = " "
def press(var):
    global input
    input = input + str(var)
    equation.set(input)

def equalpress():
    try:
        global input
        total = str(eval(input))
        equation.set(total)
        input = ""
    except:
        equation.set(" error ")
        input = ""

def clear():
    global input
    input = " "
    equation.set(" ")


Calwindow = Tk()
Calwindow.title("Calculator")
Calwindow.geometry("330x150")
Calwindow.resizable(False, False)
equation = StringVar()

ttk.Entry(Calwindow,textvariable=equation).grid(columnspan=4 , padx= 60 , pady= 4)
ttk.Button(Calwindow, text="7", command=lambda:press(7)).grid(column=1, row=1)
ttk.Button(Calwindow, text="4", command=lambda:press(4)).grid(column=1, row=2)
ttk.Button(Calwindow, text="1", command=lambda:press(1)).grid(column=1, row=3)
ttk.Button(Calwindow, text="C", command=lambda:press(clear())).grid(column=1, row=4)
ttk.Button(Calwindow, text="8", command=lambda:press(8)).grid(column=2, row=1)
ttk.Button(Calwindow, text="5", command=lambda:press(5)).grid(column=2, row=2)
ttk.Button(Calwindow, text="2", command=lambda:press(2)).grid(column=2, row=3)
ttk.Button(Calwindow, text="0", command=lambda:press(0)).grid(column=2, row=4)
ttk.Button(Calwindow, text="9", command=lambda:press(9)).grid(column=3, row=1)
ttk.Button(Calwindow, text="6", command=lambda:press(6)).grid(column=3, row=2)
ttk.Button(Calwindow, text="3", command=lambda:press(3)).grid(column=3, row=3)
ttk.Button(Calwindow, text="=", command=equalpress).grid(column=3, row=4)
ttk.Button(Calwindow, text="+", command=lambda:press("+")).grid(column=4, row=1)
ttk.Button(Calwindow, text="-", command=lambda:press("-")).grid(column=4, row=2)
ttk.Button(Calwindow, text="*", command=lambda:press("*")).grid(column=4, row=3)
ttk.Button(Calwindow, text="/", command=lambda:press("/")).grid(column=4, row=4)
Calwindow.mainloop()