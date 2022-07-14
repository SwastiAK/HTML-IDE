# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:55:21 2022

@author: Swasti
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background = "lightblue")

open_img = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/HTML IDE/open.png"))
save_img = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/HTML IDE/save.png"))
exit_img = ImageTk.PhotoImage(Image.open("C:/Users/Swasti/Desktop/Python Projects/HTML IDE/exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80, bg = "pink", fg = "black")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title = "Open HTML File", filetypes = (("HTML Files", "*.html"), ))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END, formated_name)
    root.title(formated_name)
    html_file = open(name,'r')
    paragraph = text_file.read()
    my_text.insert(END, paragraph)
    html_file.close()

open_button=Button(root, image = open_img, text="Open File", command = openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button=Button(root, image = save_img, text="Save File")
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)

exit_button=Button(root, image = exit_img, text="Exit File")
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)
    
root.mainloop()