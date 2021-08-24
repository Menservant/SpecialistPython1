# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# # что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

path = "data.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в той же папке что и текущий файл


f = open(path, "r", encoding="UTF-8")
len_symb = 0
count_lem = 1
for line in f:
    line = line.strip()
    len_symb += len(line)
    if len(line) == 0 :
         count_lem+=1

    # print(line)
print(f"Непробельных символов: {len_symb}")
print(f"Количество стихов : {count_lem}")

# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.
