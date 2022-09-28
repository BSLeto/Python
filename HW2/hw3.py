# 3. Задайте список из n чисел последовательности
# (1+1\n)**n и выведите на экран их сумму.


n = int(input('Введите число: '))
numbers_list = []
for i in range(1, n + 1):

    numbers_list.append([i, (1+(1//i))**i])
dict_numbers = dict(numbers_list)
print(dict_numbers)
print(f'Сумма чисел последовательности = {sum(dict_numbers.values())}')