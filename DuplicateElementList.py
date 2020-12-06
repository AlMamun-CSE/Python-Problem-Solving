my_list = [1,1,2,3,4,5,5]
my_dict = {}
for (ind,elem) in enumerate(my_list):
    if elem in my_dict:
        my_dict[elem].append(ind)
    else:
        my_dict.update({elem:[ind]})

for key,value in my_dict.items():
    if len(value) > 1:
        print("key(%s) has indices (%s)" % (key, value))
