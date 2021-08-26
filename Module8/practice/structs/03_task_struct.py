# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

lst = [random.randint(-100, 100) for i in range(10)]
print(lst)
lst1 = [el for el in lst if el <= 10]
print(lst1)
lst2 = [el for el in lst if el >= 0]
print(sum(lst2))
lst3 = [el for el in lst if el % 2 == 0]
print(sum(lst3)/len(lst3))
