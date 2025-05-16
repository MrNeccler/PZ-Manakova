def lowercase_generator(input_string):
    for char in input_string:
        yield char.lower()

# Пример использования
input_str = "Hello World! Привет, Мир! 123"
result = [char for char in lowercase_generator(input_str)]
print(''.join(result))  # Выведет: "hello world! привет, мир! 123"