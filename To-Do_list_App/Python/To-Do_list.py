from tkinter import messagebox
from tkinter import *
import sqlite3 as sql

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
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            task.remove(the_value)
            list_update()
            the_cursor.execute("Delete from task where title = ?",(the_value))
    except:
        messagebox.showinfo("Error","No task selected . cannot delete")

def delete_all_tasks():
    messagebox = messagebox.askyesno("Delete All" , "Are you sure ?")
    if messagebox == True:
        while(len(task) != 0):
            task.pop()
        the_cursor.execute("delete from task")
        list_update()

def clear_list():
    task_listbox.delete(0,"delete from task")

def close():
    print(tasks)
    window.destroy()

def retrieve_database():
    while(len(tasks) != 0):
        task.pop()
    for row in the_cursor.execute("select title from tasks"):
        task.append(row[0])
if __name__ == "__main__":
    window = Tk()
    canvas = Frame(window , width = 400 , height= 500 )
    canvas.pack()
    the_connection = sql.connect("listoftasks.db")
    the_cursor = the_connection.cursor()
    the_cursor.execute("create table if not exists tasks (title here)")
    tasks = []
    lable = Label(canvas,text= "To - Do List",font=( "arial" ,25 , "bold"), foreground= "black")
    entry_box = Entry(canvas , font= ("arial" , 14) , foreground= "black" , background= "white")

    lable.place(x = 110 , y = 20)

    window.mainloop()