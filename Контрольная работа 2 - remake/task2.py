import re


string = input("Ввод: ")


def is_leap_year(year):
    # Високосный год: делится на 4 и (не делится на 100 или делится на 400)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Регулярное выражение даты (dd/mm/yyyy)
pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/((1[6-9])[0-9]{2}|[2-9][0-9]{3})$'

# Проверка на соответствие регулярному выражению
if not re.match(pattern, string):
    print(f"Дата: {string} не является валидной")
    exit()

# Разделяем день, месяц, год
day, month, year = map(int, string.split('/'))

# Список дней в месяце для обычного года
days_in_month = [31, (29 if is_leap_year(
    year) else 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= day <= days_in_month[month - 1]:
    print(f"Дата: {string} является валидной")
else:
    print(f"Дата: {string} не является валидной")
