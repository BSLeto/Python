# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random


list_length = int(input("Введите длинну списка: "))
list_numbers = []
new_num = 0 
for i in range(list_length):
      new_num = round(random.uniform(0.00, 10.00), 2)
      list_numbers.append(new_num)
print(list_numbers)
max_num = round(list_numbers[0] % 1, 2)
min_num = round(list_numbers[0] % 1, 2)
list = [num % 1 for num in list_numbers if num % 1 > 0.1]

print(round(max(list), 2))
print(round(min(list), 2))
print(round((max(list) - min(list)), 2))