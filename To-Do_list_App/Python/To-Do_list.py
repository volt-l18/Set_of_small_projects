from tkinter import messagebox
import tkinter as tk
import sqlite3 as sql
window = tk.Tk()
canvas = tk.Canvas(window , width = 400 , height= 300 )
canvas.pack()

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0 :
        messagebox.showinfo("feild is empty")
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks value(?)',(task_string))
        list_update()
        task_field.delete(0,"end")

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert("end",task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in task:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute("delete task from task  =?",(the_value))
    except:
        messagebox.showinfo("error" , "no task selected cannot delete")

def delete_all_tasks():
    pass

labeltitle = tk.Label(window, text='To - Do List')
labeltitle.config(font=('helvetica', 20))
canvas.create_window(200, 25, window=labeltitle)

entry = tk.Entry(window) 
canvas.create_window(200, 75, window=entry ,width = 300)

window.mainloop()