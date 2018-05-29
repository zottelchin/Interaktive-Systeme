import turtle

def drawTest():
    abraham = turtle.Turtle()
    abraham.begin_fill()
    abraham.color("yellow")
    for i in range (0,4):
        abraham.forward(90)
        abraham.right(90)

    turtle.done()