lst1 = []
lst1 = [int(item) for item in input().split()]
lst1.sort()
New_Bajet = int(input())
k = 2
count = 0
sum = 0
for i in lst1:
    if i <= k:
        sum += i
        count = count + 1

sub = New_Bajet - sum
total_sub_len = len(lst1) - count
result = sub / total_sub_len
print("%.2f" % result)
