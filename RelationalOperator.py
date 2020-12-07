T = int(input())
N = []
for i in range(T):
    x, y = map(int, input().split())
    if x > y:
        print(">")
    elif x < y:
        print("<")
    elif x == y:
        print("=")
