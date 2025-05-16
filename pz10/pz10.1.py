def find_guest_visitor(students_visits):
    # Создаем множество всех студентов
    all_students = set(students_visits.keys())
    
    # Проверяем для каждого студента, посещал ли он всех остальных
    for student, visited in students_visits.items():
        # Множество студентов, которых посетил текущий студент (исключая себя)
        visited_without_self = visited - {student}
        
        # Если посетил всех остальных, возвращаем этого студента
        if visited_without_self == all_students - {student}:
            return student
    
    # Если такого студента нет, возвращаем None
    return None

# Пример данных: ключ - имя студента, значение - множество студентов, у которых он был в гостях
students_data = {
    "Алексей": {"Мария", "Иван", "Елена"},
    "Мария": {"Алексей", "Иван"},
    "Иван": {"Алексей", "Мария", "Елена"},
    "Елена": {"Алексей", "Иван"}
}

# Ищем студента, который был в гостях у всех
result = find_guest_visitor(students_data)

if result:
    print(f"Студент {result} побывал в гостях у всех остальных студентов.")
else:
    print("В группе нет студента, который побывал в гостях у всех остальных.")