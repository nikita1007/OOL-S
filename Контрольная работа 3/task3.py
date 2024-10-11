### Задание 1: Кашееды 
n = int(input("Введите количество детей, любящих манную кашу: "))
m = int(input("Введите количество детей, любящих овсяную кашу: "))

# Те, кто любит манную кашу
print("\nВвод фамилий тех, кто любит манную кашу:")
semolina = set()
for _ in range(n):
    semolina.add(input().strip())

# Те, кто любит манную кашу
print("\nВвод фамилий тех, кто любит овсянную кашу:")
oatmeal = set()
for _ in range(m):
    oatmeal.add(input().strip())

# Пересечение тех, кто любит обе каши
both = semolina.intersection(oatmeal)

if both:
    print(f"\nКоличество детей любящие обе каши: {len(both)}")
else:
    print("\nТаких нет")
