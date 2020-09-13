from graphics import *
win = GraphWin( "Fine House", 300, 300)


house = Rectangle(Point(175,175), Point(225,225))
house.setFill ('red')
house.draw(win)

leftRoofLine = Line(Point(175,175), Point(200,140))
leftRoofLine.draw(win)

rightRoofLine = Line(Point(200,140), Point(225,175))
rightRoofLine.draw(win) 

door = Rectangle(Point(190,200), Point(210,225))
door.setFill ('tan')
door.draw(win)

window = Rectangle(Point(210,185), Point(220,195))
window.setFill ('light green')
window.draw(win) 

center = Point(50,50)
sun = Circle(center, 25)
sun.setFill ('yellow')
sun.draw(win)

labelPoint = Point(80,270)
textLabel = Text(labelPoint, "Click on Sun!")
textLabel.draw(win)

win.getMouse()

#creates a setting sun that moves and changes color of sun, background, and window color
sun.move(50,200)
sun.setFill('orange') 
win.setBackground ("dark blue")
window.setFill('yellow')











