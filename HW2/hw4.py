# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число: '))
list_numbers = []
for i in range(-N, N+1):
    list_numbers.append(i)
print (list_numbers)
f = open('text.txt')
first_pos = int(f.readline())
second_pos = int(f.readline())
print (first_pos, second_pos)
result = list_numbers[first_pos-1]*list_numbers[second_pos-1]
print (result)