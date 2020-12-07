import re
S = input()
capital = re.findall('([A-Z])', S)
smallest = re.findall('([a-z])', S)
number = re.findall('([0-9])', S)
symbol = re.findall('([@_!#$%^&*()<>?/|}{~:.,])', S)

print(*capital)
print(*smallest)
print(*number)
print(*symbol)
