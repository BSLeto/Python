# print('hello world')

# Типы данных и переменные

# a = 123
# b = 1.23
# print(type(a) , type(b) )
# s = 'hello world'
# print(type(s), s)

# f = True

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
# print(list)

# Ввод и вывод данных

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())

# print(a, ' + ', b, '=', a+b)

# Важно и нужно, без них вы не напишете ни одной программы
# Если помните математику – проблем не будет
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет
# a = 1.312312
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a += 5

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# f = [1,2,3,4,5,6,7,8,9,10]
# print(2 in f)
# Условия
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# Управляющие конструкции: while

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Знакомьтесь – range
# r = range(100, 0, -20)  # range(100, 0, -20)
# for i in r:
#     print(i)
# # 100 80 60 40 20
# for i in range(5):
#     print(i)
# # 0 1 2 3 4


# Строки
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#     print(c)
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])  # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2]  # ...


# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [12, 2, 3, 4, 5]

# функция Это фрагмент программы, используемый
# многократно

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# print(f(1)) 