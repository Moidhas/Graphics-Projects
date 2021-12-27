from math import *
from random import *
from tkinter import *
myWindow = Tk()
screen = Canvas( myWindow, width=600, height=600, background = "white" )
screen.pack()

for n in range (15000):
    x1 = randint(0,600)
    x2 = x1 + 4
    y1 = randint (0,600)
    y2 = y1 + 4
    ds = sqrt((300-x2)**2+ (300 - y2)**2)
    if ds <= 75:
        screen.create_oval(x1,y1,x2,y2, fill = "red", outline = "red")
    elif ds <= 150:
        screen.create_oval(x1,y1,x2,y2, fill = "light blue", outline = "blue")
    elif ds <= 225:
        screen.create_oval(x1,y1,x2,y2, fill = "lawn green", outline = "green")
    else:
        screen.create_oval(x1,y1,x2,y2, fill = "black", outline = "black")



        

