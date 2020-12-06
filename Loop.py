import turtle

# turtle.speed(1)
#
# for i in range(4):
#
#     turtle.forward(100)
#     turtle.left(90)
#
# turtle.exitonclick()
result = 0
num = 1
for i in range(50):
    result = result + num
    print(f"{i} + {num} = {result }")
    num += 1
print(result)
