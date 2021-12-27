from time import *
from random import *
from tkinter import *
from math import *
myWindow = Tk()
screen = Canvas( myWindow, width=800, height=500, background = "black" )
screen.pack()

x = - 100
y = 200
x2 = x + 100
y2 = y + 100
xSpeed = 8
eValue = 300
Mouthspeed = 3.5
sValue = (360 - eValue)/2


#Pellete
def Pele (x1):
    for i in range (5):
        pellets = screen.create_oval(x1,250,x1+25,250+25,fill = "blue", outline = "blue")
        x1 = x1 + 150
        screen.update()
        sleep(0.05)

Pele(100)

#Pacman moving
for f in range (1000):

    Pacman = screen.create_arc(x,y,x2,y2, fill = "yellow", start = sValue, extent = eValue)
    Trail = screen.create_rectangle(x-100,y,x,y2, fill = "black", outline = "black")
    screen.update()
    sleep(0.03)
    screen.delete(Pacman)
    
    eValue = eValue + Mouthspeed

    if eValue > 355:
        Mouthspeed = -1 * Mouthspeed

    elif eValue < 300:
        Mouthspeed = -1 * Mouthspeed
         
    x = x + xSpeed
    x2 = x + 100

    sValue = (360 - eValue)/2

    if x > 800:
        x = -100
        x2 = x + 100
        Pele(100)
   
    


    

   
