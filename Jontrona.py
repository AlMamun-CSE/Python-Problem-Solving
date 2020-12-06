def solve(N, M, K):
    a = N % M
    for i in range(K):
        a = (a * a + a) % M
    return a


T = int(input())
for i in range(T):
    n, m, k = map(int, input().split())
    result = solve(n, m, k)
    print(f"Case #{i + 1}:", result)
