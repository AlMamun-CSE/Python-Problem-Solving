# dictionary practise in python 
bd_division_info = {"Barishal": {"district": 6, "upazila": 39, "union": 333},
                    "Dhaka": {"district": 13, "upazila": 93, "union": 1833},
                    "Chittagong": {"district": 11, "upazila": 97, "union": 336},
                    "Khulna": {"district": 10, "upazila": 59, "union": 270},
                    "Mymensingh": {"district": 4, "upazila": 34, "union": 270},
                    "Rajshahi": {"district": 8, "upazila": 70, "union": 558},
                    "Rangpur": {"district": 8, "upazila": 58, "union": 536},
                    "Sylhet": {"district": 4, "upazila": 38, "union": 334}}
print(bd_division_info)
print(bd_division_info.keys())
for division in bd_division_info:
    print("Division:", division, " Upazila:", bd_division_info[division]["upazila"])
print(bd_division_info.popitem())
print(bd_division_info)
print(bd_division_info.popitem())
print(bd_division_info.__delitem__("Rajshahi"))
print(bd_division_info)


