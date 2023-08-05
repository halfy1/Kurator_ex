def calculate_sum(s):
    while '>2' in s or '>3' in s or '>4' in s:
        s = s.replace('>2', '33>', 1)
        s = s.replace('>3', '4>', 1)
        s = s.replace('>4', '2>', 1)
    return sum(int(c) for c in s if c.isdigit())

s = ">"+20*"2"+30*"3"+40*"4"
result = calculate_sum(s)
print(f"Эрик должен Артёму {result} рублей.")
