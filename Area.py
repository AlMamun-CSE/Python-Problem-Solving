def area(x):
    return x*2 - 4


b = int(input())
for i in range(b):
    c = int(input())
    print(f'Case {i + 1}: {area(c)}')
