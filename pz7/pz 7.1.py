def swap_case(text):
    result = []
    for char in text:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
# Пример использования
input_string = "Привет, Hello! Это Тест 123"
output_string = swap_case(input_string)
print(output_string)