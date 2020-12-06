Array = [2, 10, 47, 42, 6, 15]
N = len(Array)


def bubble_sort(array, n):
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


print(bubble_sort(Array, N))
