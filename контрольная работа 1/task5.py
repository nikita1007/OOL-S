n = int(input("Введите число n: "))


def squares(number: int) -> None:
    for i in range(number+1):
        print(i**2)

print("Результат выполенения программы:")
squares(number=n)
