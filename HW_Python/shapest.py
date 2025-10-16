import turtle

y = turtle.Screen()
board = turtle.Turtle()
y.bgcolor('white')

#square
def square() :
    board.setx(-100)
    board.sety(0)
    for _ in range(4) :
        board.pencolor('orange')
        board.forward(100)
        board.left(90)
    board.pendown()    

#triangle
def triangle() :
    board.penup()
    board.goto(50,100)
    board.pendown()
    board.fillcolor('red')
    for _ in range(3) :
        board.pencolor('purple')
        board.forward(100) #draw base
        board.left(120)

#hexagon
def hexagon() :
    board.penup()
    board.goto(-25,-75)
    board.pendown()
    for _ in range(6) :
        board.pencolor('blue')
        board.forward(90)
        board.left(300)

# Draw the polygons
square()
triangle()   
hexagon()

turtle.done()