from graphics import * 
win = GraphWin("My Circle", 500, 500) 

h = Circle(Point(250,165), 50)
h.setFill("black")
h.draw(win)

e1 = Circle(Point(235,140), 10)
e1.setFill("white")
e1.draw(win)

e2 = Circle(Point(265,140), 10)
e2.setFill("white")
e2.draw(win)

ant1 = Line(Point(235,115),Point(230,85))
ant1.setFill("Black")
ant1.draw(win)

ant2 = Line(Point(265,115),Point(270,85))
ant2.setFill("black")
ant2.draw(win)

b = Circle(Point(250,250), 100)
b.setFill("yellow")
b.draw(win)

s1 = Oval( Point(160,185),Point(340,235))
s1.setFill("black")
s1.draw(win)

s2 = Oval(Point(153,245),Point(348,295))
s2.setFill("black")
s2.draw(win)

s2 = Oval(Point(178,310),Point(320,330))
s2.setFill("black")
s2.draw(win)

w = Line(Point(250,350),Point(250,150))
w.setFill("black")
w.draw(win)

win.getMouse() # pause for click in window
win.close() 