#blahBlahBlah Blah\
from tkinter import*
import random

root = Tk()
root.geometry("1000x1000")
root.title("Blah Blah")
label = Label(root,text = "Gess")

def diy():
    colors = ["grey","red","blue","orange","green"]
    number = random.randint(0, 4)
    colorname = colors[number]
    root.configure(background = colorname)
    colors1 = random.randint(0, 4)
    colorname1 = colors[colors1]
    label['fg'] = colorname1
btn = Button(root,text = "Start",command = diy)
btn.pack()
label.pack()
root.mainloop()