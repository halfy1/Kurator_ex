def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_debt():
    for debt in range(5000000, 1000000, -1):
        if '228' in str(debt) and str(debt).count('7') == 3:
            if is_prime(debt):
                return debt + 100000

print(f"Друзья отдали Сгущенке {find_debt()} рублей.")

