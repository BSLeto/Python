#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# day = int(input("Введите цифру обозначающую день недели: "))
# if 5 < day < 8:
#     print("Выходной")
# elif 0 < day < 6:
#     print("рабочий день")
# else:
#     print("Такого дня нет")


day_week = int(input('Введите день недели: '))
 
res = lambda day_week: day_week == 6 or 7


if res == True:
    print('Да,это день является выходным')
else:
    print('Нет, этот день не является выходным')