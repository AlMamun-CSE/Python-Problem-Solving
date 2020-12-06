# def isPrime(n):
#     # Corner case
#     if n <= 1:
#         return False
#
#     # Check from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# # Driver Program to test above function
# n = int(input())
# if isPrime(n):
#     print("Yes")
# else:
#     print("No")
import math


def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n % i == 0:
            return False
    return True


T = int(input())
for i in range(T):
    N = int(input())
    if isPrime(N):
        print("Prime")
    else:
        print("Not prime")

