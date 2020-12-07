a = int(input())
add = 0
if a > 0:
    for i in range(1, a+1):
        add = add + i
else:
    for i in range(a, -1):
        add = add+i
print(add)
