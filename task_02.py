# 2) Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Insert num: '))
sum_num = 1
list_num = []
for i in range(1, n + 1):
    list_num.append(i)
    sum_num *= i
print(list_num)
print(sum_num)

