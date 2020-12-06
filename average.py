number = int(input(" Enter below number you enterested: "))
a = []
for i in range(number):
    n = int(input())
    a.append(n)
ave = sum(a) / number

"""
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
    """
print("Average Number: ", round(ave, 2))
print(type(a))
