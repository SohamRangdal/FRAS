"""
messagebox.showinfo("notification", f" Welcome {collection.find} \n\n Login Successfull", parent=window,
                    command=main_window())

elif collection.find_one(
    {"Username": ad_txt1.get(), "Password": ad_txt2.get(), "Role": "HOD", "Department": dpt_list.get()}):
messagebox.showinfo("notification", f" Welcome {ad_txt1.get()} \n\n Login Successfull", parent=window,
                    command=main_window())

elif collection.find_one(
    {"Username": ad_txt1.get(), "Password": ad_txt2.get(), "Role": "Employee", "Department": dpt_list.get()}):
messagebox.showinfo("notification", f" Welcome {ad_txt1.get()} \n\n Login Successfull", parent=window,
                    command=main_window())


"""
#***************************************************************************************************************
"""
department = collection2.find({}, {"_id": 0})
x = [D['Dpt_name'] for D in department ]

role = collection3.find({}, {"_id":0})
y = [R['Role'] for R in role]


dpt = tk.Label(login, text="Department", height=1, fg="white", bg="#5b5a5b", font=('arial', 15, ' bold '))
dpt.place(x=15, y=230)
n = tk.StringVar()
dpt_list = ttk.Combobox(login, width=15, textvariable=n)
dpt_list['values'] = x
dpt_list.place(x=110, y=230)

rle = tk.Label(login, text="Role", height=1, fg="white", bg="#5b5a5b", font=('arial', 15, ' bold '))
rle.place(x=15, y=190)
m = tk.StringVar()
rle_list = ttk.Combobox(login, width=15, textvariable=m)
rle_list['values'] = y
rle_list.place(x=110, y=190)
"""



#Section Head


import tkinter as tk

from tkinter import *

from tkinter import messagebox, Text, ttk

window = tk.Tk()
window.geometry('450x680')
window.resizable(0, 0)
window.configure(background="#2b2b2b")






window.mainloop()