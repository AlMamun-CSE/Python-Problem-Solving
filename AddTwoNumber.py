print("Hello, Welcome!")


def add_two_number(first, second):
    return f"{first} + {second} = {first + second}"


a, b = map(int, input("Enter Two Number: ").split())
sums = add_two_number(a, b)
print(sums)
