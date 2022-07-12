# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:55:21 2022

@author: Swasti
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background = "lightblue")

open_img = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/ADV-C160-Student/open.png"))
save_img = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/ADV-C160-Student/save.png"))
exit_img = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/ADV-C160-Student/exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80, bg = "pink", fg = "black")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

root.mainloop()