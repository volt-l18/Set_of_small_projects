from tkinter import *
from tkinter import ttk
Calwindow = Tk()
Calwindow.title("Calculator")
frm = ttk.Frame(master=Calwindow, padding=10 )
frm.grid()
ttk.Button(frm, text="7", command=Calwindow.destroy).grid(column=0, row=1)
ttk.Button(frm, text="4", command=Calwindow.destroy).grid(column=0, row=2)
ttk.Button(frm, text="1", command=Calwindow.destroy).grid(column=0, row=3)
ttk.Button(frm, text="C", command=Calwindow.destroy).grid(column=0, row=4)
ttk.Button(frm, text="8", command=Calwindow.destroy).grid(column=1, row=1)
ttk.Button(frm, text="5", command=Calwindow.destroy).grid(column=1, row=2)
ttk.Button(frm, text="2", command=Calwindow.destroy).grid(column=1, row=3)
ttk.Button(frm, text="0", command=Calwindow.destroy).grid(column=1, row=4)
ttk.Button(frm, text="9", command=Calwindow.destroy).grid(column=2, row=1)
ttk.Button(frm, text="6", command=Calwindow.destroy).grid(column=2, row=2)
ttk.Button(frm, text="3", command=Calwindow.destroy).grid(column=2, row=3)
ttk.Button(frm, text="=", command=Calwindow.destroy).grid(column=2, row=4)
ttk.Button(frm, text="+", command=Calwindow.destroy).grid(column=3, row=1)
ttk.Button(frm, text="-", command=Calwindow.destroy).grid(column=3, row=2)
ttk.Button(frm, text="*", command=Calwindow.destroy).grid(column=3, row=3)
ttk.Button(frm, text="/", command=Calwindow.destroy).grid(column=3, row=4)
Calwindow.mainloop()