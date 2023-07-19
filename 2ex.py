from itertools import product

# Задаем параметры
letters = 'АЛНИШ'
length = 6
max_diff = 100

# Генерируем все возможные слова
words = [''.join(word) for word in product(letters, repeat=length)]

# Вычисляем количество слов, удовлетворяющих условию
count = 0
for i in range(len(words)):
    word = words[i]
    if abs(i - words.index(word[::-1])) <= max_diff:
        count += 1

# Выводим результат
print(count)