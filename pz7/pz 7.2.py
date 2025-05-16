def reverse_words(s):
    words = s.split()  # Разбиваем строку на слова (автоматически удаляет лишние пробелы)
    reversed_words = words[::-1]  # Разворачиваем список слов
    return ' '.join(reversed_words)  # Соединяем слова через один пробел

# Пример использования
input_string = "  один   два   три   четыре  пять  "
output_string = reverse_words(input_string)
print(output_string)