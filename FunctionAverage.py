def AverageList(lis):
    add = sum(lis)
    length = len(lis)
    average = add / length
    return average


def Namotha(n=1):
    for i in range(1, 11):
        print(f"{n} x {i} = ", n * i)


lis = [1, 2, 3, 4, 5]
print(AverageList(lis))

# Print Namath

# default
print(Namotha())
# Assigned Value
print(Namotha(4))
