# Задание 1
best_score = 0

while True:
    score = int(input('Введите результат: '))
    if score == -1:
        break
    if score > best_score:
        best_score = score

print(best_score)



# Задание 2
best_score = 0
friends_count = 0

while True:
    score = int(input())
    if score == -1:
        break
    friends_count += 1
    if score > best_score:
        best_score = score

print(friends_count)



# Задание 3
total_income = 0  
citizens_count = 0  

while True:
    income = int(input('Введите доход: '))  
    if income == 0:        
        break
    total_income += income  
    citizens_count += 1     

average_income = total_income / citizens_count if citizens_count > 0 else 0
print(average_income)



# Задание 4
X = int(input("Введите целое число X: "))

current_sum = 0
for i in range(1, X + 1):
    current_sum += i
    print(current_sum)



# Задание 5
def is_perfect(num):
    if num <= 1:
        return False
    sum_divisors = 1  # 1 является делителем для любого числа > 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:  # Добавляем парный делитель
                sum_divisors += num // i
    return sum_divisors == num

N = int(input("Введите число N: "))
count = 0

for num in range(2, N + 1):
    if is_perfect(num):
        count += 1

print(count)



# Задание 6
n = int(input('Введите натуральное число ступеней: '))

for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * i
    print(spaces + stars)



# Задание 7
while True:
    user_input = input("Введите число: ") 
    
    try:
        number = int(user_input) 
        print(f"Введено целое число: {number}")
        break
    except ValueError:
        print("Ошибка. Попробуйте еще раз.", end=" ")



# Задание 8
# Блок 1: 123...n * 8 + n = 987... (убывающая последовательность)
for n in range(1, 10):
    left = ''.join(str(i) for i in range(1, n + 1))
    right = ''.join(str(i) for i in range(9, 9 - n, -1))
    print(f"{left} * 8 + {n} = {right}")

print()

# Блок 2: 123...n * 9 + (n + 1) = 111... (n+1 единиц)
for n in range(1, 10):
    left = ''.join(str(i) for i in range(1, n + 1))
    right = '1' * (n + 1)
    print(f"{left} * 9 + {n + 1} = {right}")

print()

# Блок 3: 111... * 111... = 123...n...321 (симметричное число)
for n in range(1, 10):
    ones = '1' * n
    square = int(ones) ** 2
    print(f"{ones} * {ones} = {square}")



# Задание 9
n = int(input("Введите число N: "))

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

for number in range(2, n + 1):
    if is_prime[number]:
        print(number)  # Каждое число выводится с новой строки



# Задание 10
n = int(input("Введите число N: "))

for num in range(2, n + 1):
    sum_divisors = 1  # 1 — делитель для любого числа > 1
    # Перебираем возможные делители до √num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            # Добавляем парный делитель (если он не равен i)
            if i != num // i:
                sum_divisors += num // i
    if sum_divisors == num:
        print(num)
