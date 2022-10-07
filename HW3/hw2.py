# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def mult_list_nums(num_list):
    count = 0
    new_list = []
    if not len(num_list) % 2 == 0:
        count = int((len(num_list) + 1) / 2)
    else:
        count = int((num_list) / 2)
    for i in range(count):
        new_list.append(num_list[i]*(num_list[len(num_list) - i - 1]))
    return new_list

my_list = [2, 3, 4, 5, 6]
print (my_list)
print (mult_list_nums(my_list))
