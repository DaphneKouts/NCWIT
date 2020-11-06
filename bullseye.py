#Daphne Koutsoukos
from graphics import *
win = GraphWin("My Circle", 500, 500)

red1 = Circle(Point(250,250), 120)
red1.setFill("red")
red1.setOutline("red")
red1.draw(win)

white1 = Circle(Point(250,250), 100)
white1.setFill("white")
white1.setOutline("white")
white1.draw(win)

blue1 = Circle(Point(250,250), 80)
blue1.setFill("blue")
blue1.setOutline("blue")
blue1.draw(win)

red2 = Circle(Point(250,250), 60)
red2.setFill("red")
red2.setOutline("blue")
red2.draw(win)

white2 = Circle(Point(250,250), 40)
white2.setFill("white")
white2.setOutline("white")
white2.draw(win)

blue2 = Circle(Point(250,250), 20)
blue2.setFill("blue")
blue2.setOutline("blue")
blue2.draw(win)

win.getMouse() # pause for click in window
win.close()
