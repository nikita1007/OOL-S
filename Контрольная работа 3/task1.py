def fill_snake_matrix(n: int, m: int) -> list:
    res = [[] for _ in range(n)]
    
    for i in range(n):
        if i % 2 == 0:
            # Заполнение слева направо
            for j in range(m):
                res[i].append(i * m + j + 1)
        else:
            # Заполнение справа налево
            for j in range(m):
                res[i].insert(0, i * m + j + 1)
    
    return res

n, m = map(int, input("Введите размер матрицы (n, m): ").split())

snake_matrix = fill_snake_matrix(n=n, m=m)
longest_number_cd = len(str(max(num for row in snake_matrix for num in row)))

# Табличный вывод
for sublist in snake_matrix:
    print("".join(f"{num:>{longest_number_cd+1}}" for num in sublist))
