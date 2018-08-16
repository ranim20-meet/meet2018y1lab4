import turtle

turtle.shape('turtle')
finn = turtle.clone()
finn.shape('square')
finn.color('yellow')
finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)
charlie = turtle.Turtle()
charlie.shape = ('triangle')
charlie.color('blue')
charlie.goto(100,100)
charlie.goto(200,0)
charlie.goto(0,0)

finn.goto(-400,100)
finn.stamp()
finn.goto(-100,100)
charlie.goto(-400,-100)
charlie.stamp()
charlie.goto(-100,-100)

turtle.mainloop()

