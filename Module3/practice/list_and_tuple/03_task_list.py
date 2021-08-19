# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.
import random

n = int(input("Enter number of elements")
mas = []
s = 0
i = 0
for i in range(n):
    mas.append(random.randint(0, 100))
    s += mas[i]
print(mas)
print(s)
