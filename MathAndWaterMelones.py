M, K = map(int, input().split())
# remainder = N % M
# print(remainder)

a = M / K
b = int(a)
c = b * K
d = M - c
print(d)
