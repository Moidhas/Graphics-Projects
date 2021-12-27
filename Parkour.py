from math import*
from tkinter import *
myWindow = Tk()
screen = Canvas( myWindow, width=800, height=600, background = "sky blue" )
screen.pack()

from time import *

#BACKGROUND

#- Building
screen.create_rectangle(50,200,300,600, fill = "grey")

#- Windows
gy = 250
for glass in range(2):
    screen.create_rectangle(100,gy,150,gy + 100, fill = "white", outline = "black", width = 5)
    screen.create_rectangle(200,gy,250,gy + 100, fill = "white", outline = "black", width = 5)
    gy = gy + 150

# - door
screen.create_rectangle(150,525,200,600,fill = "red", outline = "gold", width = 3)
screen.create_oval(195,560,197,562, fill ="brown")

#- Building #2
screen.create_rectangle(550,100,800,600, fill = "grey")

#- Windows #2
gy = 150
for glass in range(3):
    screen.create_rectangle(600,gy,650,gy + 100, fill = "white", outline = "black", width = 5)
    screen.create_rectangle(700,gy,750,gy + 100, fill = "white", outline = "black", width = 5)
    gy = gy + 150

# - door # 2
screen.create_rectangle(640,560,720,600,fill = "red", outline = "gold", width = 3)
screen.create_oval(710,580,712,582, fill ="brown")

#dirt
screen.create_rectangle(300,590,550,600, fill = "tan4",outline = "forest green", width = 3)

#Variable used to create falling
i = 0
g = 0

#Animation Variables Robot
xs =150
ys = 190
#Animation Variables Police
xsp = 60
xsp2 = 80
xpeye = 70

#animation running
for f in range (1000):
    #Shoes Robot 
    s1 = screen.create_oval(xs,ys,xs + 10,ys + 9,fill = "black")
    s2 = screen.create_oval(xs + 20,ys,xs + 30,ys + 9,fill = "black")
    #Body Robot
    b1 = screen.create_oval(xs,ys - 64.8,xs + 30,ys + 5, fill = "grey",outline = "grey")
    
    #eye Robot
    e1 = screen.create_oval(xs,ys - 40,xs + 30,ys - 20, fill = "white", outline = "grey")
    e2 = screen.create_oval(xs + 10,ys-35,xs + 20,ys - 25, fill = "black")


    #Shoes Police
    sp1 = screen.create_oval(xsp,190,xsp + 10,199,fill = "white",outline = "blue",width = 2)
    sp2 = screen.create_oval(xsp2,190,xsp2 + 10,199,fill = "white", outline = "blue", width = 2)

    #Body Police
    bp1 = screen.create_oval(xsp,125.2,xsp2 + 10,195, fill = "blue",outline = "white", width = 2)

    #Eye Police
    ep1 = screen.create_oval(xsp,150,xsp2 + 10,170, fill = "white", outline = "grey")
    ep2 = screen.create_oval(xpeye,155,xpeye + 10,165, fill = "black")

    #Police Hat
    Phat = screen.create_polygon(xpeye,125,xsp,100,xpeye + 5,105,xpeye + 15,105,xpeye + 10,125, fill = "blue", outline = "white", width = 2)


    screen.update()
    sleep(0.03)
    screen.delete(s1,s2,b1,e1,e2,sp1,sp2,bp1,ep1,ep2,Phat)
    

    #Translations 
    if xsp2 != 205:
        xsp = xsp + 5
        xsp2 = xsp2 + 5
        xpeye = xpeye + 5
        xs = xs + 5

    elif xs <= 514:
        xs = xs + 2*i
        ys = 0.2*i**2 - 2.2*i + ys
        i = i + 0.9
        
    
    elif xs > 514 and ys < 580:
        ys = ys + 5
        
 
        

#Animation jumping
#for fr in range (1000):
    
    #Shoes Police
    #sp1 = screen.create_oval(xsp,190,xsp + 10,199,fill = "white",outline = "blue",width = 2)
    #sp2 = screen.create_oval(xsp2,190,xsp2 + 10,199,fill = "white", outline = "blue", width = 2)

    #Body Police
    #bp1 = screen.create_oval(xsp,125.2,xsp2 + 10,195, fill = "blue",outline = "white", width = 2)

    #Eye Police
    #ep1 = screen.create_oval(xsp,150,xsp2 + 10,170, fill = "white", outline = "grey")
    #ep2 = screen.create_oval(xpeye,155,xpeye + 10,165, fill = "black")

    #Police Hat
    #Phat = screen.create_polygon(xpeye,125,xsp,100,xpeye + 5,105,xpeye + 15,105,xpeye + 10,125, fill = "blue", outline = "white", width = 2)

    





#Draws grid lines, spaced 50 pixels apart.  This helps you plan your scene.
spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line( x, 25, x, 1000, fill="blue")
    screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line( 25, y, 1000, y, fill="blue")
    screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W)
