T = int(input())
li = [0] * T
for i in range(T):
    n = int(input())
    li[i] = n

for x in range(len(li)):
    s = (li[x] * li[x]) % 10
    print()
