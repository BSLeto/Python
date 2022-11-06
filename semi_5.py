# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1].
# Найдите это число.

# ===================================================
# my_string = "1 2 3 4 5 7 8 9"

# my_list = list(map(int, my_string.split()))
# for i in range(1, len(my_list)):
#     if my_list[i] - my_list[i-1] > 1:
#         print(my_list[i]-1)

# ===================================================

# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# def new_list(my_string):
#     if my_string[0] == max(my_string):
#         return new_list(my_string[1:])
#     else:
#         myList = [my_string[0]]
#         for i in range(1,len(my_string)):
#             if myList[-1] < my_string[i]:
#                 myList.append(my_string[i])    
#         return myList
    
# print(new_list(my_list))

        # ===================================================

        # Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Lorem Ipабвsum - это табвекст-"рабвыба", частабво используемый в печати и вабвэбабв-дизайне.\
    Lorem Ipsum является стандартнабвой "рыбоабвй" для текстоабвв на латинице с начала XVI века.'


my_text = list(filter(lambda x: 'абв' not in x, text.split()))


print(" ".join(my_text))
    