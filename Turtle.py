import turtle
turtle.shape("circle")

# trangle
# for i in range(3):
#     turtle.forward(100)
#     turtle.left(120)
turtle.speed(1)
for side_length in range(50, 100, 1):
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.penup()
    turtle.forward(3)
    turtle.left(93)
    turtle.pendown()
turtle.exitonclick()

