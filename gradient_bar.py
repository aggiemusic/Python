from graphics import *
win = GraphWin( "Gradient Bar", 400, 300)



c = 0
xa = 0
xb = 0
for bars in range(6):
    bars = Rectangle(Point(xa ,0), Point(xa + 67,300))
    c = c + 20
    bars.setFill( color_rgb( 0, c, 0 ) )
    bars.setWidth(0)
    bars.draw(win)
    xa = xa + 67
    bars2 = Rectangle(Point(xb ,0), Point(xb + 268,300))
    bars2.setFill( color_rgb( 0, c, 0 ) )
    bars2.setWidth(0)
    bars2.draw(win)
    xb = xb + 268
    
    
    
    
    
    
    