'''Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры.'''
import random


def pr():
    # Генерируем четырехзначное число
    number = random.randint(1000, 9999)
    return number


def has(number):
    # Преобразуем число в строку и создаем множество для проверки уникальности
    digits = str(number)
    return len(set(digits)) < len(digits)


def main():
    number = pr()
    print(f"Сгенерированное число: {number}")

    if has(number):
        print("В числе есть одинаковые цифры.")
    else:
        print("В числе нет одинаковых цифр.")
        
main ()
