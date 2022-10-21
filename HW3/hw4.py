# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print ('Введено не число')
        result = -1
    return result

num = int_input("Введите число: ")
print(f'{num} => {bin(num)[2:]}')