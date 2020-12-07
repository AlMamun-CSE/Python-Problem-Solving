import re
T = int(input())

for i in range(T):
    symbol = input()
    try:
        print(re.compile(symbol))
    except:
        print("False")
