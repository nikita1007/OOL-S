# Задание 5: *Самое часто встречающееся слово

words = input("Введите слова (через пробел):\n").split(' ')

# Получаем сет из слов (слова без повтора)
words_unique = set(words)

# Список "слово": "количество его встреч в массиве `word`"
word_count = dict()
for word in words_unique:
    word_count[word] = words.count(word)

# Находим слово с максимальным количеством вхождений
max_count = 0
most_frequent_words = []

for word, count in word_count.items():
    if count > max_count:
        max_count = count
        most_frequent_words = [word]
    elif count == max_count:
        most_frequent_words.append(word)

# Находим лексикографически меньшее слово среди наиболее частых
result = min(most_frequent_words)

print(f"Наиболее стречаемое слово (лексикографически меньше среди других): {result}")