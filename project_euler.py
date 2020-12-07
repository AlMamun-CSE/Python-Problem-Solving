def findlengthofterm(n):
    if n == 1:
        return len(A)
    elif n == 2:
        return len(B)

    a = len(A)
    b = len(B)
    c = 0
    i = 2
    while (i < n):
        c = a + b
        a, b = b, c
        i += 1
    return c


def findIndex(n):
    if (n <= 1):
        return n

    a = len(A)
    b = len(B)
    c = 0
    res = 2

    while (c < n):
        c = a + b
        res = res + 1
        a = b
        b = c

    return res


if __name__ == '__main__':
    num = int(input())
    output = []
    for i in range(num):
        A, B, x = input().split()
        s = int(x)
        n = findIndex(s)
        a = s
        while (n > 2):
            l = findlengthofterm(n - 2)
            if a > l:
                a = a - l
            else:
                n -= 1
            n -= 1

        if n == 1:
            output.append(A[a - 1])
        else:
            output.append(B[a - 1])

    for out in output:
        print(out)