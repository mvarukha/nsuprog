# Задание 1
bitcoin_price = int(input('Введите стоимость биткоина в рублях: '))
bitcoin_price = str(bitcoin_price)
print(bitcoin_price[-3])

# Задание 2
time = int(input('Введите целое число в диапазоне от 1 до 86400: '))
if time % 3600 == 0:
    print(time // 3600, 'часов ', '0 минут ', '0 секунд')
elif time % 3600 != 0 and (time % 3600) % 60 == 0:
    print(time // 3600, 'часов ', (time % 3600) // 60, 'минут')
elif time % 3600 != 0 and (time / 3600) % 60 != 0:
    print(time // 3600, 'часов ', (time % 3600) // 60, 'минут', (time % 3600) % 60, 'секунд')

# Задание 3
number = int(input('Введите число: '))
print(number % 2)

# Задание 4
X, Y, N = map(int, input("Введите X рублей, Y копеек и N заказов через пробел: ").split())

# Общий доход в рублях и копейках
total_rubles = X * N           # Общие рубли
total_cents = Y * N            # Общие копейки

# Копейки в рубли
total_rubles += total_cents // 100  # Добавляем полные рубли от копеек
total_cents = total_cents % 100      # Оставшиеся копейки


print(f"{total_rubles} руб., {total_cents} коп.")

# Задание 5
a = '(\\___/)'
b = '(=\'.\'=)'
c = '(\")_(\")'
m = int(input('Сколько зайцев вы хотите? '))
print(a * m + '\n' + b * m + '\n' + c * m + '\n')

# Задание 6
k = input('Введите число: ')
n = int(input('Сколько раз подряд это число записали без пробелов? '))
r = int(input('На что умножили число? '))
print(int(k * n) * r)

# Задание 7
raw = input('Enter number: ')
num = str(raw) # исходное int меняем на str
print(num)

# Задание 8
import math

a = float(input('Введите сторону а: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону с: '))

# Существует ли треугольник?
if a + b > c and a + c > b and b + c > a:
    # Углы в радианах
    angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    # Преобразуем радианы в градусы
    angle_A_deg = math.degrees(angle_A)
    angle_B_deg = math.degrees(angle_B)
    angle_C_deg = math.degrees(angle_C)

    print(angle_A_deg)
    print(angle_B_deg)
    print(angle_C_deg)
else:
    print("Треугольник с такими сторонами не существует.")

# Задание 9
att = int(input('Введите количество попыток паса: '))
cmp = int(input('Введите количество завершений: '))
yds = int(input('Пасовые ярды: '))
td = int(input('Пасы приземления: '))
iNt = int(input('Перехваты: '))
a = (cmp/att - 0.3) * 5
b = (yds/att - 3) * 0.25
c = (td/att) * 20
d = 2.375 - ((iNt/att)*25)
Passer_rating = ((a + b + c + d)/6)*100
print(Passer_rating)

# Задание 10
# Даны два целых числа Х и Y. Если X делится на Y или Y делится на X, то -1, иначе - другое число
x = int(input('Введите х: '))
y = int(input('Введите у: '))
print(int(x % y == 0 or y % x == 0))

# Задание 11
degrees = float(input('Введите градусы: '))
if degrees % 30 == 0:
    print(degrees // 30, 'часов ', ' 0 минут')
elif degrees % 30 != 0:
    print(degrees // 30, 'часов ', (degrees % 30) / 0.5, 'минут')

# Задание 12
import datetime
now = datetime.datetime.now()
print(now)

# Задание 13
N = int(input("Введите количество строк на странице: "))
C = int(input("Введите количество столбцов на странице: "))
record_number = int(input("Введите номер записи в справочнике: "))

# номер страницы
page_number = (record_number - 1) // (N * C) + 1

# номер записи на странице
record_on_page = (record_number - 1) % (N * C)

# номер строки и столбца
row_number = (record_on_page % N) + 1
column_number = (record_on_page // N) + 1

print(f"страница {page_number} столбец {column_number} строка {row_number}")
