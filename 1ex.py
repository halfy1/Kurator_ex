from itertools import product

# Задаем параметры
digits = '0123456'
length = 5

# Генерируем все возможные числа
numbers = [''.join(number) for number in product(digits, repeat=length) if number[0] != '0']

# Фильтруем числа, удовлетворяющие условиям задачи
result = []
for number in numbers:
    if any(digit in '0246' for digit in number) and number.count('3') == number.count('5'):
        result.append(number)

# Выводим результат
print(len(result))