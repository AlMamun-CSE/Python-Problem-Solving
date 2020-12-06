# def is_palindrome(s):
#     l = len(s)
#     indx1 = l // 2 - 1
#     indx2 = (l + 1) // 2
#     while indx1 >= 0 and indx2 < l:
#         if s[indx1] != s[indx2]:
#             return False
#         indx1, indx2 = indx1 - 1, indx2 + 1
#
#     return True


def is_palindrome(s):
    return s == s[::-1]


S = input()
result = is_palindrome(S)
if result:
    print("Yes")
else:
    print("No")
