from graphics import * 
win = GraphWin("My Circle", 500, 500) 

bg = Rectangle(Point(0,0), Point(500,500))
bg.setFill("white")
bg.setOutline("blue")
bg.draw(win)

b = Circle(Point(250,250), 100)
b.setFill("Orange")
b.draw(win)

s1 = Oval(Point(160,168), Point(250,335))
s1.setFill("black")
s1.draw(win)

o1 = Oval(Point(158,170), Point(245,330))
o1.setFill("orange")
o1.setOutline("orange")
o1.draw(win)

s2 = Oval(Point(340,170), Point(250,335))
s2.setFill("black")
s2.draw(win)

o2 = Oval(Point(342,172), Point(255,330))
o2.setFill("Orange")
o2.setOutline("orange")
o2.draw(win)

l1 = Rectangle(Point(248,150), Point(252,350))
l1.setFill("black")
l1.draw(win)

l2 = Rectangle(Point(150,248), Point(350,252))
l2.setFill("black")
l2.draw(win)

t1 = Text(Point(250,100),"Come support CTK basketball")
t1.setTextColor("blue")
t1.setSize(25)
t1.draw(win)

t2 = Text(Point(250,375),"Versus Port Jefferson @4:15")
t2.setTextColor("blue")
t2.setSize(25)
t2.draw(win)

t3 = Text(Point(250,450),"Home this saturday at the CTK gym")
t3.setTextColor("blue")
t3.setSize(23)
t3.draw(win)

win.getMouse() # pause for click in window 
win.close()  