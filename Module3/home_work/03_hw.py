# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random
n = 10
numbers = []
i = 0
sum = 0
while i < n:
    numbers.append(random.randint(-100,100))
    print(f"Element{i} = {numbers[i]}")
    if numbers[i] > 0 and numbers[i] % 2 == 0:
        sum += numbers[i]
    i += 1
print(sum)
