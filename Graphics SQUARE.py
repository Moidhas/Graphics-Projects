from math import * 
from tkinter import *
myWindow = Tk()
screen = Canvas( myWindow, width=800, height=600, background = "white" )
screen.pack()





widhtS = int(input("Please input the width s of a square:  "))
widhtT = int(input("Please input the width t of a smaller square:  "))
startT = (widhtS - widhtT)/2 + 100


#Start Square
screen.create_rectangle(100,100, widhtS + 100, widhtS + 100, fill = "orange")

#Yellow square
screen.create_rectangle(startT,startT,widhtT + startT, widhtT + startT, fill = "yellow")

#1 square
screen.create_rectangle(100,100, startT, (widhtS + widhtT)/2 + 100, fill ="blue" ,outline = "black")


#2 square
screen.create_rectangle(100, (widhtS + widhtT)/2 + 100, (widhtS + widhtT)/2 + 100, widhtS + 100, fill = "green", outline = "black")


#3 square
screen.create_rectangle((widhtS + widhtT)/2 + 100, widhtS + 100, widhtS + 100, startT, fill = "red")





