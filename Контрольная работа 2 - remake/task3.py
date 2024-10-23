sequence = [12345, -54323, 50003, 13, -33, 33, 3333,
            3332, 33333, 44333, 55553, 66663, 100003, -100000, 54321]

def count_valid_triplets(sequence):
    # Находим максимальный элемент, который является пятизначным числом и оканчивается на 3
    max_element = max([x for x in sequence if 10000 <= abs(
        x) <= 99999 and abs(x) % 10 == 3], default=None)

    # Если такого элемента нет, то возвращаем 0, так как нет смысла проверять тройки
    if max_element is None:
        return 0

    # Подсчитываем количество троек, которые удовлетворяют условиям
    count = 0
    n = len(sequence)

    # Проход по всем тройкам
    for i in range(n - 2): 
        triplet = sequence[i:i+3]
        # Проверяем, что хотя бы один элемент оканчивается на 3
        if any(abs(x) % 10 == 3 for x in triplet):
            # Проверяем сумму тройки
            if sum(triplet) <= max_element:
                count += 1

    return count


result = count_valid_triplets(sequence)
print(result)
