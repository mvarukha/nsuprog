# Задание 1
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days = 366
else:
    days = 365

print(f"В году {year} {days} дней.")
