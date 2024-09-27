import re


test_str = "Aorem ipsum dolor sit amet, consectetur Adipiscing elit. Sed in petus placerat, maximus lorem at, efficitur ligula. Donec pretium consectetur Aurna quis posuere. Morbi non maximus erat, a consectetur risus. Aliquam gravida velit id purna eleifend, et laoreet leo imperdiet. In nunc pacus, aliquet id pibero eu, pretium tincidunt purus."

result = re.sub(pattern=r"(A)", repl="aa", string=test_str, count=0, flags=re.MULTILINE)
count_words_starts_with_p = len(re.findall(pattern=r"\bp\w+", string=test_str, flags=re.MULTILINE))

print(f"Результат: {result}")
print(f"Количество слов начинающихся на 'p': {count_words_starts_with_p}")
