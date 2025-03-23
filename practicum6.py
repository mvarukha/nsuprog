# Задание 3
# Подсказка для ввода
print("Введите размеры района в формате NxM:")
print("Пример: 4x2")

# Ввод размеров района
size_input = input().strip()  # Читаем размеры района
N, M = map(int, size_input.split('x'))  # Разделяем на N и M

# Подсказка для ввода K
print("Введите количество кварталов K:")
print("Пример: 6")

# Ввод количества кварталов
K = int(input().strip())  # Читаем K

# Проверка условий
if K <= N * M and (K % N == 0 or K % M == 0):
    print("Результат: успешно")
else:
    print("Результат: неосуществимо")
