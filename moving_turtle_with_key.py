import turtle

turtle.shape('turtle')

def turtle_forward():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_backward():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_reset():
    turtle.reset()

turtle.onkey(turtle_forward, 'w')
turtle.listen()

turtle.onkey(turtle_left,'a')
turtle.listen()

turtle.onkey(turtle_backward, 's')
turtle.listen()

turtle.onkey(turtle_right, 'd')
turtle.listen()

turtle.onkey(turtle_reset, 'Escape')
turtle.listen()
