#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

lst = [randint(1,9) for i in range(randint(4,9))]
if len(lst) % 2 == 0:
    x = lst[:len(lst) // 2]
    y = lst[:len(lst)//2 -1:-1]
else:
    x = lst[:len(lst) // 2 + 1]
    y = lst[:len(lst)//2 - 1:-1]

f = lambda a, b: a * b
c = list(map(f,x,y))
print("Старый список ",lst)
print("Новый список  ", c)

