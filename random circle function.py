import random
from graphics import *
from time import sleep
win = GraphWin("MyCircle",500,500)
numCircles = 0
radius = 40
x = 50
y = 50
color = "peachpuff"
def myCircle(win,x,y,radius,color):
    '''You choose the color, size, and position in a window a circle will be.'''
    circle = Circle(Point(x,y), radius)
    circle.setFill(color)
    circle.draw(win)   


while numCircles < 1000:
    myCircle(win, x, y, radius, color)
    x = random.randint(10,490)
    y = random.randint(10,490)
    radius = random.randint(10,100)
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    color = color_rgb(R,G,B)
    numCircles = numCircles + 1

win.getMouse() # pause for click in window 
win.close()  