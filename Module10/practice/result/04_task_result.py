# Одноклеточная амеба каждые 3 часа делится на 2 такие же амёбы.
# Необходимо определить, сколько будет амеб через n часов, если первоначально была только одна амёба.
# Формат входных данных: Вводится целое положительное число n.
# Формат выходных данных: Требуется одно число — конечное число амеб.
# 21 1+ 21/3*2
n = int(input("Enter number of hours: "))
print(f"Result is {n//3*2+1}")
