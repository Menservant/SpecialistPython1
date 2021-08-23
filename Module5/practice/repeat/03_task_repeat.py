def palindrome(of, to):
    for number in range(of, to):
        number = str(number)
        rev_number = number[::-1]
        mas = []
        if (number == rev_number) == True:
            mas.append(number)
        return mas


print(palindrome(10, 100))
