# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке
import math


def palindrome(number):
    rev = 0
    number1 = number
    while number > 0:
        n = number % 10
        math.floor(n)
        rev = rev * 10 + n
        number /= 10
    if rev == number1:
        return "Polindrome"
    else:
        return "Not a polindrome"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
