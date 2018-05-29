import turtle

rect_Height = 50
rect_Width = 50

turtle.tracer(0, 0)
turtle.setup(rect_Width*5,rect_Height*10)

screen = turtle.Screen()
screen.colormode(255)
screen.setworldcoordinates(0,-10*rect_Height,5*rect_Width,0)

buddha = turtle.Turtle()
buddha.speed("fastest")
buddha.hideturtle()



def drawHeatmap(matrix):
    for i in range(5):
        for j in range(10):
            buddha.fillcolor(intToColor(matrix[j][i]))
            drawSqare(i*rect_Width,j*-rect_Height)
    screen.update()

def drawSqare(x,y):
    buddha.penup()
    buddha.goto(x,y)
    buddha.pendown()
    buddha.begin_fill()
    for i in range(2):
        buddha.forward(rect_Width)
        buddha.right(90)
        buddha.forward(rect_Height)
        buddha.right(90)
    buddha.end_fill()

def intToColor(i):
    i //= 64
    if i < 256:
        return(0,i,255)
    elif 256 <= i < 512:
        i -= 256
        return(0,255,255-i)
    elif 215 <= i < 768:
        i -= 512
        return(i,255,0)
    elif 768 <= i < 1024:
        i -= 768
        return (255,255-i,0)
    else:
        return (255,000,42)
    print("Changed color")