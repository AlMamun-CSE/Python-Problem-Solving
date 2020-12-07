H, M = map(int, input().split())

if 0 <= H < 12 and 0 <= M < 60:
    a = H - (M / 5)
    print("First Time: ", a)
    if a < 0:
        a = (a * (-1) * 30) - (0.5 * M)
        print("Second Time(a<0): ", a)
    else:
        a = a * 30 + 0.5 * M
        print("Third Time(a not < 0): ", a)
    if a > 180:
        print(360 - a)
    else:
        print(a)
