import re


string = input("Ввод: ")

pattern = r'(.)\1{4,}'

# Функция для замены найденных подстрок
def replacer(match):
    char = match.group(1)
    count = len(match.group(0))
    return f'{char}{{{count}}}'

# Замена всех найденных подстрок с помощью функции replacer
result = re.sub(pattern, replacer, string)

print(f"Вывод: {result}")
