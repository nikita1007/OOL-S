import re


input_number = input("Введите число: ") 

pattern = r"^[+-]?(?P<integer>\d*)(\.(?P<fractional>\d+))?$"
matches = re.match(pattern=pattern, string=input_number, flags=re.MULTILINE)
[integer, fractional] = matches.groupdict(default=0).values()

print(f"Целая часть: {integer} (кол-во знаков: {len(str(integer))})\nДробная часть: {fractional} (кол-во знаков: {len(str(fractional))})")
