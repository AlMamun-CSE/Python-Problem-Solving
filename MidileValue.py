import random

a, b = None, None


# Returns the correct position of
# pivot element

def Partition(arr, l, r):
    lst = arr[r]
    i = l
    j = l

    while j < r:

        if arr[j] < lst:
            arr[i], arr[j] = arr[j], arr[i]

            i += 1

        j += 1

    arr[i], arr[r] = arr[r], arr[i]

    return i


# Picks a random pivot element between
# l and r and partitions arr[l..r]
# around the randomly picked element
# using partition()

def randomPartition(arr, l, r):
    n = r - l + 1

    pivot = random.randrange(1, 100) % n

    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]

    return Partition(arr, l, r)


# Utility function to find median

def MedianUtil(arr, l, r, k, a1, b1):
    global a, b

    # if l < r

    if l <= r:

        # Find the partition index

        partitionIndex = randomPartition(arr, l, r)

        # If partion index = k, then

        # we found the median of odd

        # number element in arr[]

        if partitionIndex == k:

            b = arr[partitionIndex]

            if a1 != -1:
                return

                # If index = k - 1, then we get

        # a & b as middle element of

        # arr[]

        elif partitionIndex == k - 1:

            a = arr[partitionIndex]

            if b1 != -1:
                return

                # If partitionIndex >= k then

        # find the index in first half

        # of the arr[]

        if partitionIndex >= k:

            return MedianUtil(arr, l, partitionIndex - 1, k, a, b)

            # If partitionIndex <= k then

        # find the index in second half

        # of the arr[]

        else:

            return MedianUtil(arr, partitionIndex + 1, r, k, a, b)

    return


# Function to find Median

def findMedian(arr, n):
    global a

    global b

    a = -1

    b = -1

    # If n is odd

    if n % 2 == 1:

        MedianUtil(arr, 0, n - 1, n // 2, a, b)

        ans = b;

        # If n is even

    else:

        MedianUtil(arr, 0, n - 1, n // 2, a, b)

        ans = (a + b) // 2

        # Print the Median of arr[]

    print("Median = ", ans)


# Driver code

n = int(input())
li = list(map(int, input().strip().split()))[:n]
n = len(li)
if n % 2 != 0 and 1 <= n <= 1000001:
    print(findMedian(li, n))



