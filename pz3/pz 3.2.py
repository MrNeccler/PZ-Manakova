'''Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим'''



 def find_middle_number(a, b, c):
    # Создаем список из трех чисел
    numbers = [a, b, c]
    # Сортируем список
    numbers.sort()
    # Возвращаем среднее число (второй элемент после сортировки)
    return numbers[1]
# Пример использования
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
middle_number = find_middle_number(num1, num2, num3)
print("Среднее число из введенных:", middle_number)
