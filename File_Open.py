with open("sexpire.txt", mode='r') as s_file:
    word_all = []
    for line in s_file.readlines():
        word = line.strip().split(" ")
        word_all += word

    unique_item = set(word_all)
    print(len(unique_item))
    print(len(word_all))

with open("unique_list.txt", mode="w") as w_file:
    for item in sorted(unique_item):
        w_file.write(item)
        w_file.write("\n")
print("finished")

S = "MY Name is, al Mamun"
print(S.split(","))
