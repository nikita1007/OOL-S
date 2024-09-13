n = int(input("Введите число 'n': "))


def calculate_sequence(n: int) -> float:
    result = 1
    
    for i in range(2, n+1):
        result += 1/i**2
    
    return result


print(f"Результат выполения: {calculate_sequence(n=n)}")
