X, Y = map(int, input().split())

remainder = Y % X
if remainder != 0:
    result = X - remainder
    print(result)
else:
    print(remainder)
