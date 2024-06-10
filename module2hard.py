def find_pairs(n):
    pairs = []
    for i in range(1, 21):
        for j in range(i, 21):
            if (i + j) % n == 0:
                pairs.append(f"{i}{j}")
    return "".join(pairs)
n = int(input("Введите число от 3 до 20: "))
result = find_pairs(n)
print(f"Нужный пароль для числа {n}: {result}")