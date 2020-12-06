import turtle

result = 0
for num in range(100):
    if num % 5 == 0:
        print(num)
        result += num
print("Sum is:", result)

# turtle.shape("turtle")
# turtle.speed(1)
#
# for side_length in range(50, 100, 10):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
#
# turtle.exitonclick()

import turtle

turtle.color("black")
turtle.speed(1)

counter = 0
while counter < 2:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()
