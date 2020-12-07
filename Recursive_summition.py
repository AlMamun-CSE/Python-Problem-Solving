def getSum(lst, n):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + getSum(lst[1:], n)


l1 = []
N = int(input())
if 1 <= N <= 100:
    for i in range(N):
        li = list(map(int, input().strip().split()))
        li.__delitem__(0)
        length = len(li)
        result = getSum(li, length)
        l1.append(result)

for i in range(len(l1)):
    print("Case %d: %d" % i + 1 % (l1[i]))
