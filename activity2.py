from tkinter import *
from datetime import date

window=Tk()
window.title("Getting started with the widgets")
window.geometry("400x300")
window.config(bg="#15285C")

lbl=Label(text="Hey There!",fg="white",bg="#15285C",height=1,width=300)
lbl.pack()
name_lbl=Label(text="Full name",fg="white",bg="#15285C",height=1,width=300)
name_lbl.pack()
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to the application.\ntoday's date is"
    greet=f"hello {name}\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

name_entry.pack()
text_box=Text(height=3)
text_box.pack()
btn=Button(text="Greet",command=display,height=1,fg="white",bg="#008500")
btn.pack()
window.mainloop()