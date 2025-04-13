# Задание 1
# Ввод данных
N, d, R = map(int, input().split())

# Вычисление длины цепочки
L = 2 * R * N + d * (N - 1)

print(L)


# Задание 2
import math

number = float(input("Введите положительное число, большее 2: "))

if number <= 2:
    print("Число должно быть больше 2.")
else:
    # Извлечение квадратного корня до тех пор, пока результат не станет меньше 2
    while number >= 2:
        print(f"{number:.3f}")  # Форматированный вывод с тремя знаками после запятой
        number = math.sqrt(number)

    # Вывод последнего значения, которое меньше 2
    print(f"{number:.3f}")


# Задание 3
def find_group_size(N):
    # Начинаем с наименьшего возможного делителя (2) и идем вверх
    for i in range(2, N + 1):
        if N % i == 0:
            return i
    # Если делителей больше 1 нет, возвращаем N (группа из N человек)
    return N

N = int(input())

print(find_group_size(N))


# Задание 4
def can_build_network(N):
    return N % 2 == 0 and N >= 4

successful_teams = 0

while True:
    N = int(input())
    if N == 0:
        break
    if can_build_network(N):
        successful_teams += 1

print(successful_teams)


# Задание 5
def is_palindrome(s):
    # Проверяем, является ли строка палиндромом
    return s == s[::-1]

def find_mileage():
    for N in range(100000, 1000000):
        # Последние пять цифр N — палиндром
        last_five_N = str(N)[-5:]
        if not is_palindrome(last_five_N):
            continue

        # Последние пять цифр N+1 — палиндром
        last_five_N1 = str(N + 1)[-5:]
        if not is_palindrome(last_five_N1):
            continue

        # Средние четыре цифры N+2 — палиндром
        middle_four_N2 = str(N + 2)[1:5]
        if not is_palindrome(middle_four_N2):
            continue

        # Все шесть цифр N+3 — палиндром
        all_six_N3 = str(N + 3)
        if not is_palindrome(all_six_N3):
            continue

        # Если все условия выполнены
        return N

    # Если решение не найдено
    return None


result = find_mileage()
print(result)


# Задание 6
def find_cab():
    for ab in range(10, 100):
        # Вычисляем квадрат AB
        cab = ab * ab
        # Проверяем, что результат трехзначный
        if 100 <= cab <= 999:
            # Преобразуем числа в строки
            ab_str = str(ab)
            cab_str = str(cab)
            # Проверяем, что CAB начинается с C
            if cab_str[0] == ab_str[0]:
                # Выводим результат
                return cab
    # Если решение не найдено
    return None

# Находим и выводим результат
result = find_cab()
print(result)


# Задание 7
from itertools import permutations

# Буквы, которые нужно заменить на цифры
letters = 'SENDMORY'

# Перебираем все возможные комбинации цифр
for perm in permutations(range(10), len(letters)):
    # Сопоставляем буквы с цифрами
    S, E, N, D, M, O, R, Y = perm
    
    # Проверяем, что S и M не равны 0
    if S == 0 or M == 0:
        continue
    
    # Вычисляем SEND, MORE и MONEY
    SEND = 1000 * S + 100 * E + 10 * N + D
    MORE = 1000 * M + 100 * O + 10 * R + E
    MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y
    
    # Проверяем, выполняется ли равенство
    if SEND + MORE == MONEY:
        print(f"SEND = {SEND}, MORE = {MORE}, MONEY = {MONEY}")
        break
else:
    print("Решение не найдено.")


# Задание 8
x = int(input("Введите натуральное число x: "))

# Счетчик способов
count = 0

# Перебираем все возможные значения a от 1 до sqrt(x)
for a in range(1, int(x**0.5) + 1):
    b_squared = x - a**2  
    b = int(b_squared**0.5)  # b как целое число

    # является ли b^2 натуральным числом и соответствует ли условию
    if b_squared > 0 and b**2 == b_squared and a <= b:
        count += 1

print(f"Количество способов представления числа {x} в виде суммы квадратов двух натуральных чисел: {count}")


# Задание 9
def total_dots(N):
    total = 0
    for a in range(N + 1):
        for b in range(a, N + 1):
            total += a + b
    return total

N = int(input())

print(total_dots(N))


# Задание 10
def count_staircases(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for j in range(N + 1):
        dp[0][j] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j > i:
                dp[i][j] = dp[i][i]
            else:
                dp[i][j] = dp[i - j][j - 1] + dp[i][j - 1]
    
    # количество всех возможных лесенок, включая случай с одним рядом
    return dp[N][N]


N = int(input())


print(count_staircases(N))
