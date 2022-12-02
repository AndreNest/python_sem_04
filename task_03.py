# 3) Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 4];
# - [2, 3, 5, 6] => [12, 15]
list_num = [2, 3, 4, 5, 6, 10, 20]
new_list = []
if len(list_num) % 2 == 0:
    for i in range(len(list_num)//2):
        new_list.append(list_num[i] * list_num[len(list_num) - 1 - i])
else:
    for i in range(len(list_num)//2):
        new_list.append(list_num[i] * list_num[len(list_num) - 1 - i])
    new_list.append(list_num[(len(list_num) // 2)])

print(new_list)

