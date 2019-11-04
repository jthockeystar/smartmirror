import random
#from  graphics import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import *
import os
from tkinter import font
import time
#def exit(event):
 #   root.destroy()

smartmirror = tk.Tk()

w, h = smartmirror.winfo_screenwidth(), smartmirror.winfo_screenheight()
print("w h success")
smartmirror.geometry("%dx%d+0+0" % (w, h))
print("geometry success")
#var = StringVar()
#print("var success")
#font1 = font.Font("Times", "123")
label = tk.Label(smartmirror, text="hello world", bg="blue", font=("Times", 200), height=h, width=w)
#label = Label(smartmirror, text="PASS", bg="green", fg="black", font=(None, 15), height=50, width=50)
print("label success")
label.pack()
print('label pack success')
#smartmirror.overrideredirect(1)
print("overrideredirect success")

smartmirror.mainloop()
print("loop success")
