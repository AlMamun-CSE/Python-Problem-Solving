T = int(input())
li = [0]*T


def distance(x1,y1,x2,y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**.5
    return dist


for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    li[i] = x1, y1, x2, y2

    print(distance(x1, y1, x2, y2))

