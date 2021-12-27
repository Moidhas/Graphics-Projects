from math import*
from tkinter import *
from time import *
from random import *
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background = "white" )
screen.pack()

#Court
screen.create_rectangle(0,500,800,800, fill = "blanched almond")

#Net
screen.create_line(50,700,50,550,150,450, fill = "black",width = 15)
screen.create_line(150,350,150,500,300,450,300,325,150,350,fill = "grey",width = 10)
screen.create_line(200,410,250,400,250,460,200,475,200,410,fill = "black", width = 6)
screen.create_oval(295,470,200,500,outline = "orange",width = 5)
screen.create_oval(300,600,400,700,outline = "white", width = 5)

#LOGO
screen.create_text(350,650, text = "YMCA", fill = "red", font = "slant 20")

#Mesh
for f in range (50):
    randx = randint(215,275)
    randy = randint(500,550)
    screen.create_line(randx,500,randx,randy,fill = "white",width =3)

#free throw line
screen.create_arc(550,800,450,500,start = -90, extent = 180, outline = "white",width = 5)

#center circle
screen.create_oval(750,500,1050,800,fill = "orange",outline = "white", width = 5)
screen.create_oval(790,600,875,700,fill = "blue" ,outline = "white", width = 5)

#ANIMATION
for f in range(500):

    x1 = -5*f + 700
    x2 = x1 + 50
    y1 = .11*f**2 - 12*f + 600
    y2 = y1 + 50

    ball = screen.create_oval(x1,y1,x2,y2, fill = "orange")

    screen.update()
    sleep(0.03)
    screen.delete(ball)

    if y1 > 800:
        break
    




