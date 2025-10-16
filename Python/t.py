import turtle

# creating camvas
turtle._Screen().bgcolor("Orange")

sc = turtle._Screen()
sc.setup(400,300)

turtle.title("Welcome to turtle Window")

#turtle object creation
board = turtle.turtle()

#creating a square
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1
turtle.done()