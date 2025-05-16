people = {
    "Андрей": 178,
    "Виктор": 150,
    "Максим": 200,
    "Ольга": 165,
    "Елена": 172,
    "Дмитрий": 185
}

# Находим максимальное и минимальное значение роста
max_height = max(people.values())
min_height = min(people.values())

print(f"Наибольший рост: {max_height} см")
print(f"Наименьший рост: {min_height} см")