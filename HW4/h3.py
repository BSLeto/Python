# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

num = int(input('Введите длинну списка: '))
num_list = []
for i in range(num):
    rand_num = random.randrange(11)
    num_list.append(rand_num)
print(num_list) 
print(set(num_list))