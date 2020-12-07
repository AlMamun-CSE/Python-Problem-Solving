N = int(input())
li = []


def split(word):
    return [char for char in word]


for i in range(N):
    S = input()
    s = S.upper()
    li.append(split(s))

# res = [i for ele in li for i in ele]
print(li)
for i in range(len(li)):
    print(li[i])
