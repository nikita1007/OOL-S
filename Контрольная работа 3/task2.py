def rotate_matrix(matrix: list[list]) -> list[list]:
    n = len(matrix)
    m = len(matrix[0])

    # Создаем новый массив с размерами M x N
    rotated_matrix = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    return rotated_matrix


n, m = map(int, input("Введите размер матрицы (n, m): ").split())
matrix = [list(range(m*i+1, m*(i+1) + 1)) for i in range(n)]

rotated_matrix = rotate_matrix(matrix)
longest_number_cd = len(str(max(num for row in rotated_matrix for num in row)))

# Вывод размера "перевернутой" матрицы
print(f"{m:>{longest_number_cd+1}}{n:>{longest_number_cd+1}}")

# Табличный вывод
for sublist in rotated_matrix:
    print("".join(f"{num:>{longest_number_cd+1}}" for num in sublist))
