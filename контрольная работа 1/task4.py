
# 10243050
n = int(input("Введите число 'n': "))

def number_of_zeros(number: int) -> int:
    zeros = 0
    
    while number > 0:
        if number % 10 == 0:
            zeros += 1
        
        number = number // 10
        
    return zeros
    

print(f"Результат выполения: {number_of_zeros(number=n)}")
