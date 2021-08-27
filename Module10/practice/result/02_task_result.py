# На числовой прямой расположены точки A, B, C и D.
# Напишите программу, которая выведет, во сколько раз отрезок AB больше или меньше, чем отрезок CD.
# Формат входных данных:
# На вход программе подается четыре целых числа A, B, C и D.
# Расположение точек относительно друг друга на координатной прямой произвольное.
# Формат выходных данных:
# Выведите, во сколько раз отрезок AB больше, чем отрезок CD. Ответ введите с точностью до 6-ти знаков после запятой.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
if a > 0 and b > 0 and c > 0 and d > 0:
    ab = a - b
    cd = c - d
elif b < 0 and c < 0:
    ab = abs(b) + a
    cd = abs(c) + c
elif a < 0 and d < 0:
    ab = abs(a) + b
    cd = abs(d) + b
else:
    ab = abs(max(a, b)) - abs(min(a, b))
    cd = abs(max(c, d)) - abs(min(c, d))
    
difference = ab / cd
print(f"AB more CD in {difference} times ")

