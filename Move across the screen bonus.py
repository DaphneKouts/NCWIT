from graphics import * 
from time import sleep
win = GraphWin("My Circle", 1000, 1000) 
bg = Rectangle(Point(0,0), Point(1000,1000))
bg.setFill("black")
bg.setOutline("black")
bg.draw(win)
    

def move(x):
    b = Oval(Point(150 + x,100), Point(350 + x,400))
    b.setFill("blue")
    b.setOutline("cyan")
    b.draw(win)
    
    e1 = Oval(Point(210 + x,160), Point(225 + x,180))
    e1.setFill("white")
    e1.setOutline("cyan")
    e1.draw(win)
    
    e2 = Oval(Point(290 + x,160), Point(275 + x,180))
    e2.setFill("white")
    e2.setOutline("cyan")
    e2.draw(win)
    
    m = Oval(Point(180 + x,230), Point(325 + x,280))
    m.setFill("white")
    m.setOutline("white")
    m.draw(win)
    
    mb = Oval(Point(175 + x,220), Point(325 + x,271))
    mb.setFill("blue")
    mb.setOutline("blue")
    mb.draw(win)
    
    bl1 = Rectangle(Point(0 + x,360), Point(500 + x,410))
    bl1.setFill("black")
    bl1.setOutline("black")
    bl1.draw(win)
    
    bl2 = Polygon(Point(170 + x,360), Point(182 + x,340), Point(200 + x,360))
    bl2.setFill("black")
    bl2.setOutline("black")
    bl2.draw(win)
    
    bl3 = Polygon(Point(200 + x,360), Point(215 + x,340), Point(230 + x,360))
    bl3.setFill("black")
    bl3.setOutline("black")
    bl3.draw(win)
    
    bl4 = Polygon(Point(230 + x,360), Point(245 + x,340), Point(260 + x,360))
    bl4.setFill("black")
    bl4.setOutline("black")
    bl4.draw(win)
    
    bl5 = Polygon(Point(260 + x,360), Point(275 + x,340), Point(290 + x,360))
    bl5.setFill("black")
    bl5.setOutline("black")
    bl5.draw(win)
    
    bl6 = Polygon(Point(290 + x,360), Point(306 + x,340), Point(324 + x,360))
    bl6.setFill("black")
    bl6.setOutline("black")
    bl6.draw(win)
    sleep(.1)

    b.undraw()
    e1.undraw()
    e2.undraw()
    m.undraw()
    mb.undraw()
    bl1.undraw()
    bl2.undraw()
    bl3.undraw()
    bl4.undraw()
    bl5.undraw()
    bl6.undraw()
    
x = 1
while x < 100:
    x = x + 1
    move(x)
    
win.getMouse() # pause for click in window 
win.close()