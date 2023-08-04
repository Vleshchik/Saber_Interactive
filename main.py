def calculator(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Ошибка: неверное выражение"

# Пример использования
expression = input("Введите математическое выражение: ")
result = calculator(expression)
print("Результат:", result)