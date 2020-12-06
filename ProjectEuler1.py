import sys
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    n3 = (n - 1) // 3
    n5 = (n -1) // 5
    n15 = (n - 1) // 15

    #sum i,for i = 1 to m == m(m+1)/2
    val3 = 3 * n3 * ( n3 + 1) // 2
    val5 = 5 * n5 * ( n5 + 1) // 2
    val15 = 15 * n15 * ( n15 + 1) // 2

    total = val3 + val5 - val15
    print(total)
