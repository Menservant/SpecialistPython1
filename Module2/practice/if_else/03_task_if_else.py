# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.
a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
if a==b or c==b  or c==a:
    print("Yes")
else :
    print("No")
