import os

def find_and_count_files(filename):
    # Проверяем существование файла
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден!")
        return
    
    # Инициализируем счетчики для каждого расширения
    counters = {'.xls': 0, '.xml': 0, '.html': 0, '.css': 0, '.py': 0}
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            for ext in counters:
                if line.lower().endswith(ext):
                    counters[ext] += 1
                    total += 1
                    print(line)  # Выводим найденный файл
                    break

    # Выводим статистику
    print("\nСтатистика:")
    for ext, count in counters.items():
        print(f"{ext}: {count}")
    print(f"\nВсего найдено: {total}")

# Вызываем функцию
find_and_count_files('expansion.txt')
