# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла


def log(text, file="log.txt"):
    with open(f"{file}", "a", encoding="utf-8") as f:
            f.write(f"{text} \n")


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log011.txt")  # дописывает "message" в конец файла log01.txt
