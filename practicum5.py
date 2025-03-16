# Задание 1
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days = 366
else:
    days = 365

print(f"В году {year} {days} дней.")

# Задание 2
# координаты центра окружности и радиуса
xc = float(input("Введите координату x центра окружности (xc): "))
yc = float(input("Введите координату y центра окружности (yc): "))
r = float(input("Введите радиус окружности (r): "))

# координаты точки
x = float(input("Введите координату x точки (x): "))
y = float(input("Введите координату y точки (y): "))

# расстояние от точки до центра окружности
distance_squared = (x - xc) ** 2 + (y - yc) ** 2
r_squared = r ** 2

# положение точки относительно окружности
if distance_squared < r_squared:
    result = "Точка внутри окружности"
elif distance_squared == r_squared:
    result = "Точка на окружности"
else:
    result = "Точка вне окружности"

print(result)

# Задание 3
def check_number(num):
    # Извлекаем цифры числа
    a = num // 1000          # первая цифра
    b = (num // 100) % 10    # вторая цифра
    c = (num // 10) % 10     # третья цифра
    d = num % 10             # последняя цифра

    # Проверяем условия для "кривого" и "настоящего" числа
    if a == d and b == c:
        return "настоящее"
    else:
        return "кривое"

# Ввод числа
number = int(input("Введите четырехзначное число: "))
result = check_number(number)
print(result)

# Задание 4
def get_popugai_form(num):
    if num % 10 == 1 and num % 100 != 11:
        return "попугай"
    elif 2 <= num % 10 <= 4 and not (12 <= num % 100 <= 14):
        return "попугая"
    else:
        return "попугаев"

# Ввод числа
number = int(input("Введите натуральное число не превышающее 100: "))

# Получаем правильное склонение
popugai_form = get_popugai_form(number)

# Выводим результат
print(number, popugai_form)

# Задание 5
height = float(input('Введите рост в см: '))
weight = float(input('Введите вес в кг: '))
height = (height / 100)**2
imt = weight / height
if imt < 16:
    print('Выраженный дефицит массы тела')
if imt >= 16 and imt <= 18.49:
    print('Недостаточная масса тела')
if imt >= 18.5 and imt <= 24.99:
    print('Норма')
if imt >= 25 and imt <= 29.99:
    print('Избыточная масса тела')
if imt >= 30 and imt <= 34.99:
    print('Ожирение первой степени')
if imt >= 35 and imt <= 39.99:
    print('Ожирение второй степени')
if imt >= 40:
    print('Ожирение третьей степени')

# Задание 6
day1 = int(input("Введите количество подданных, увидевших улыбку в первый день: "))
day2 = int(input("Введите количество подданных, увидевших улыбку во второй день: "))
day3 = int(input("Введите количество подданных, увидевших улыбку в третий день: "))

counts = [day1, day2, day3]
count_repeats = 0

if counts.count(day1) > 1:
    count_repeats += 1
if counts.count(day2) > 1:
    count_repeats += 1
if counts.count(day3) > 1:
    count_repeats += 1
    
print(f"Количество повторений: {count_repeats}")

# Задание 7
def min_stations(N, K, M):
    # Расчет расстояний по часовой и против часовой стрелки
    if K < M:
        clockwise_distance = M - K - 1  # Убираем 1, так как K не считается
    else:
        clockwise_distance = N - K + M - 1  # Убираем 1, так как K не считается

    counter_clockwise_distance = N - clockwise_distance - 1  # Убираем 1, так как M не считается

    # Возвращаем минимальное расстояние
    return min(clockwise_distance, counter_clockwise_distance)

# Ввод данных
input_data = input("Введите N, K, M через пробел: ")
N, K, M = map(int, input_data.split())

# Получаем минимальное количество станций
result = min_stations(N, K, M)

# Выводим результат
print(result)

# Задание 8
def convert_knuts_to_galleons_sickles_knuts(knuts):
    # Константы для конвертации
    GALLEONS_TO_KNUTS = 17 * 29  # 1 галлеон = 493 кната
    SICKLES_TO_KNUTS = 29        # 1 сикль = 29 кнатов

    # Вычисляем количество галлеонов, сиклей и кнатов
    galleons = knuts // GALLEONS_TO_KNUTS
    remaining_knuts = knuts % GALLEONS_TO_KNUTS

    sickles = remaining_knuts // SICKLES_TO_KNUTS
    knuts = remaining_knuts % SICKLES_TO_KNUTS

    # Формируем вывод
    result = []
    if galleons > 0:
        result.append(f"{galleons} галлеонов")
    if sickles > 0:
        result.append(f"{sickles} сиклей")
    if knuts > 0:
        result.append(f"{knuts} кнатов")

    return ", ".join(result)

# Ввод количества кнатов
N = int(input("Введите количество кнатов: "))
result = convert_knuts_to_galleons_sickles_knuts(N)
print(result if result else "0 кнатов")  # Если 0, выводим 0 кнатов

# Задание 9
# Ввод высот башен
heights_input = input("Введите высоты башен через пробел: ")
heights = list(map(int, heights_input.split()))  # Преобразуем ввод в список целых чисел

# Алгоритм сортировки (пузырьковая сортировка)
for i in range(len(heights)):
    for j in range(len(heights) - 1):
        if heights[j] < heights[j + 1]:  # Сравниваем соседние элементы
            # Меняем местами, если текущий меньше следующего
            heights[j], heights[j + 1] = heights[j + 1], heights[j]

# Вывод результата
print(" ".join(map(str, heights)))  # Преобразуем список обратно в строку и выводим


# Задание 10
pin = input("Введите четырехзначный PIN-код: ")
if len(pin) == 4 and pin.isdigit() and len(set(pin)) == 4 and not (1900 <= int(pin) <= 2050):
    print("OK")
else:
    print("ERROR")
