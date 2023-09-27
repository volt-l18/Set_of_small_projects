import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window , width = 400 , height= 300 )
canvas.pack()

labeltitle = tk.Label(window, text='To - Do List')
labeltitle.config(font=('helvetica', 20))
canvas.create_window(200, 25, window=labeltitle)

entry = tk.Entry(window) 
canvas.create_window(200, 75, window=entry ,width = 300)

window.mainloop()