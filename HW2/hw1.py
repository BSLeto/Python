# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число: '))


def sumDigits(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр = {sumDigits(number)}")
