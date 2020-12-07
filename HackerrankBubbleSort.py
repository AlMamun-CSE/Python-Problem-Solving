#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    numberOfSwaps = 0

    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break
    else:
        numSwaps += numberOfSwaps
print("Array is sorted in %d swaps."%(numSwaps))
print("First Element: %d"%a[0])
print("Last Element: %d"%(a[n-1]))
