# Задание 1
number = 100  # начинаем с первого трёхзначного числа
count = 0     # счетчик чисел делящихся на 17
result = []   # список для хранения подходящих чисел

while number <= 999:
    if number % 17 == 0: 
        result.append(str(number)) 
        count += 1
    number += 1  # переход к следующему числу
print(' '.join(result))
print(count)

# Задание 2
# Задание 3
import math

def is_perfect_square(num):
    return math.isqrt(num) ** 2 == num

while True:
    num = int(input("Введите число: "))
    if is_perfect_square(num):
        print(f"Число {num} является полным квадратом")
        break
    else:
        print(f"Число {num} не является полным квадратом. Попробуйте ещё раз.")

# Задание 4

X = int(input("Введите целое число X: "))

# сумма первых X натуральных чисел
sum_numbers = X * (X + 1) // 2

# Выводим результат
print(f"Сумма первых {X} натуральных чисел равна: {sum_numbers}")

# Задание 5
N = int(input("Введите максимальный объём N (в куб. см): "))

volumes = []
k = 1  # начальная длина ребра

while True:
    volume = k ** 3  # объём текущего кубика
    if volume > N:
        break  # прекращаем, если объём превысил N
    volumes.append(volume)
    k += 1  # переходим к следующему кубику

print("Объёмы кубиков:", ' '.join(map(str, volumes)))

# Задание 6
N = int(input("Введите максимальное количество подписчиков N: "))

subscribers = 1  # начальное количество подписчиков
hour = 1         # текущий час

while subscribers <= N:
    print(subscribers)
    subscribers *= 2  # удваиваем количество подписчиков
    hour += 1         # переходим к следующему часу

# Задание 7
answer = int(input("Введите ответ Оли: "))

# является ли число степенью двойки
if answer <= 0:
    print("неверно")
else:
    # степень двойки в двоичном виде имеет одну единицу и остальные нули
    if (answer & (answer - 1)) == 0:
        print("верно")
    else:
        print("неверно")

# Задание 8
import math

N = int(input("Введите максимальное число N: "))

if N < 1:
    print("Число должно быть натуральным (≥1)")
else:
    min_questions = math.ceil(math.log2(N))
    print(f"Минимальное количество вопросов: {min_questions}")

# Задание 9
# Ввод данных (N, K, R)
N, K, R = map(float, input('Введите N K R через пробел: ').split())

day = 1          # Первый день
current = N      # Текущая длина нити

while current < R:
    current *= (1 + K / 100)  # Увеличиваем длину на K%
    day += 1                  # Переходим к следующему дню

print(day)

# Задание 10
decrease_count = 0
previous_temp = None

while True:
    temp = float(input('Введите температуру: '))
    
    if temp == 0:
        break  # Завершение ввода
    
    # Проверяем, что температура в допустимом диапазоне
    if 37.4 <= temp <= 37.8:
        if previous_temp is not None and temp < previous_temp:
            decrease_count += 1
        previous_temp = temp  # Обновляем предыдущее значение

print(decrease_count)
