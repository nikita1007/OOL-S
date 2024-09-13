sum_of_digits = 0

flag = True

while flag:
    digit = int(input())
    
    if digit == 0:
        flag = False
    
    sum_of_digits += digit

print(f"Сумма всех цифр равна {sum_of_digits}")