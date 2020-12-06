def find_median(lst):
    sorted_list = sorted(lst)
    lst_len = len(lst)
    index = (lst_len - 1) // 2

    if lst_len % 2:
        return sorted_list[index]
    else:
        return (sorted_list[index] + sorted_list[index+1]) / 2.0


n = int(input())
li = list(map(int, input().strip().split()))[:n]
if n % 2 != 0 and 1 <= n <= 1000001:
    value_of_median = find_median(li)
    print(value_of_median)
