import turtle

turtle.color("red")
turtle.speed(5)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.left(10)
    counter += 1
turtle.exitonclick()
