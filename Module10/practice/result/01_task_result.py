# Напишите программу, вычисляющую площадь всех граней и объем прямоугольного параллелепипеда.
# Формат входных данных: даны три целые числа - ширина, высота и длина параллелепипеда.
# Формат выходных данных: вывести площадь всех граней и объем фигуры

width = int(input("Enter width of figure"))
high = int(input("Enter high of figure"))
length = int(input("Enter length of figure"))
print(f"Volume of figure = {width * high * length}")
print(f"Square of figure = {2 * ((width * length)+(length * high)+(width*high))}")
