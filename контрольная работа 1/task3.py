n = int(input("Введите число 'n': "))


def fact(diget: int) -> int:
    result = 1
    
    for i in range(1, diget+1):
        result *= i
    
    return result 

def calculate_sequence(n: int) -> float:
    result = 0
    factorial = 1
    
    for i in range(1, n+2, ):
        result += 1/factorial
        factorial *= i
    
    return result

print(f"Результат выполения: {calculate_sequence(n=n):.5f}")    
    