# 5. Реализуйте алгоритм перемешивания списка.
import random


start_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_list = sorted(start_list, key=lambda *args: random.random())
print(sorted_list)