'''Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до 
B включительно; при этом каждое число должно выводиться столько раз, каково его 
значение (например, число 3 выводится 3 раза).  '''
# Вводим значения A и B
A = int(input("Введите целое положительное число A: "))
B = int(input("Введите целое положительное число B (A < B): "))
# Проверяем условие A < B
if A < B:
    for number in range(A, B + 1):
        for _ in range(number):
            print(number)
else:
    print("Ошибка: A должно быть меньше B.")
