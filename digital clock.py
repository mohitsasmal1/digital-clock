from tkinter import *
from tkinter.ttk import *
from time import strftime

c = Tk()
c.title("Digital Clock")

def time():
    String = strftime('%H:%M:%S %p')
    l.config(text = String)
    l.after(1000, time)


l = Label(c, font = ("ds-digital", 100), background = "black", foreground = "#e48af2")
l.pack(anchor = 'center')
time()

mainloop()