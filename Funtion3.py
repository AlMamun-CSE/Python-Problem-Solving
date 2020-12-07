def myfuction(x, y=10, z=0):
    # This is x,y,z local variable
    print("x = ", x, "y = ", y, "z = ", z)


# x,y,z is global variable

x = 5
y = 20
z = 15
# Assigned Argument Value
myfuction(x, y, z)
# Not Value Argument
myfuction(x, y)
myfuction(x)

