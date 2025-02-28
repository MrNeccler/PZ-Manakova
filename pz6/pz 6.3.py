def insert_first_element(A):
    if len(A) <= 1:
        return A  # Если список пуст или содержит только один элемент, возвращаем его

    first_element = A[0]  # Сохраняем первый элемент
    # Удаляем первый элемент из списка
    A = A[1:]

    # Находим правильную позицию для первого элемента
    position = 0
    while position < len(A) and A[position] < first_element:
        position += 1

    # Вставляем первый элемент на его новую позицию
    A.insert(position, first_element)
    return A

def main():
    # Пример списка
    A = [5, 1, 2, 3, 4]
    
    # Упорядочиваем список
    sorted_list = insert_first_element(A)
    
    # Выводим результат
    print("Упорядоченный список:", sorted_list)


main()
