N = int(input())
li = [0] * N

for i in range(N):
    t = int(input())
    li[i] = t

print(li[0])
for i in li:
    print((li[i] * 2 - li[i] * 2) + 2)
