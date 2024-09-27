import re


pattern = r"^#([A-Fa-f0-9]{6})$"

color_input = input("Введите значение цвета: ")
validate = re.match(pattern=pattern, string=color_input, flags=re.MULTILINE)

print("Цвет указан неверно" if validate == None else "Цвет указан верно")
