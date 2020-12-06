n = int(input())
li = []
temp = 0
rev = 0
while n > 0:
    dig = n % 10
    li.append(dig)
    n = n // 10

my_dict = {i: li.count(i) for i in li}
a = (max(my_dict, key=my_dict.get))
print(a)
dict1_doubleCond = {k: v for (k, v) in my_dict.items() if v == a}
print(dict1_doubleCond)
