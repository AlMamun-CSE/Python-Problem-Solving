N = int(input())
li = [N]
maximum = 0

li = list(map(int, input().split()))

for i in range(N):
    if li[i] > maximum:
        maximum = li[i]
print(maximum)
