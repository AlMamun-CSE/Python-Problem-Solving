N = int(input())
li = []

for i in range(N):
    a, b = map(int, input().split())
    avg = (a + b) // 2
    li.append(avg)

for i in range(len(li)):
    if li[i] % 2 == 0:
        print("Sadia will be happy.")
    else:
        print("Oops!")
