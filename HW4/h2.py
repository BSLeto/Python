# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число N: '))
mult = 2
mult_list = []
while num >= mult:
    if (num % mult) == 0:
        mult_list.append(mult)
        num /= mult
        mult = 2
    else:
        mult += 1
print(f'Множители числа: {mult_list}')
