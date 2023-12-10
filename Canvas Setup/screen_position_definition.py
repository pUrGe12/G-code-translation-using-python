import turtle

def turtle_set_up():
    '''
    I've defined a canvas (1024,600), to avoid bind and terminator issues the RUNNING parameter is manually set to true.
    
    '''
    
    screen = turtle.Screen()
    screen.title('G-code visualisation')
    screen.setup(width = 1024, height = 600) # width is the x-axis and height is the y-axis
    
    turtle.TurtleScreen._RUNNING = True
    turtle.speed(0)
    turtle.pensize(1)
    
    # start positioning
    turtle.penup()
    turtle.goto(-400, -150)
    turtle.left(90)
    
    screen.exitonclick()
    
turtle_set_up()