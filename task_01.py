# 1) Есть список: s = ['a', 'b', 'c', 'd', 'e']
# Необходимо написать программу, которая сдвинет список spisok следующим образом:\
#     ['c', 'd', 'e', 'a', 'b']

s = ['a', 'b', 'c', 'd', 'e']
b = s[2:] + s[:2]
print(b)
