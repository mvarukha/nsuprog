# Задание 1
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days = 366
else:
    days = 365

print(f"В году {year} {days} дней.")

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

# Задание 10
pin = input("Введите четырехзначный PIN-код: ")
if len(pin) == 4 and pin.isdigit() and len(set(pin)) == 4 and not (1900 <= int(pin) <= 2050):
    print("OK")
else:
    print("ERROR")
