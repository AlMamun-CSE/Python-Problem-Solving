def add_numbers(listvalu):
    sum = 0
    # for number in range(len(listvalu)): // this is list index not value
    for number in listvalu:
        print(number)
        sum += number
    return sum


result = add_numbers([1, 2, 30, 4, 5, 9])
print(result)

# Function same work Sum()function
# >>> li = [1, 2, 3]
# >>> result = sum(li)
# >>> print(result)
# 6
