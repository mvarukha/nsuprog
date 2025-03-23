# Задание 1
import math

def carpet_fit(size):
    A, B = map(int, size.split('x'))  # Разделяем входные данные на A и B
    diameter = 13
    diagonal = math.sqrt(A**2 + B**2)  # диагональ ковра

    if diagonal <= diameter:
        return "да"
    else:
        return "нет"

size_input = input("Введите размер ковровой дорожки (A x B): ")
result = carpet_fit(size_input)
print(result)

# Задание 2
# Вводим размеры отверстия
hole = input("Введите размер отверстия (AxB): ")
A, B = map(int, hole.split('x'))

# Вводим размеры кирпича
brick = input("Введите размер кирпича (CxDxE): ")
C, D, E = map(int, brick.split('x'))

# Проверяем, можно ли протолкнуть кирпич через отверстие
# Кирпич можно протолкнуть, если хотя бы одна из его сторон меньше или равна отверстию
if (C <= A and D <= B) or (C <= B and D <= A):  # Первая ориентация
    print("да")
elif (C <= A and E <= B) or (C <= B and E <= A):  # Вторая ориентация
    print("да")
elif (D <= A and E <= B) or (D <= B and E <= A):  # Третья ориентация
    print("да")
else:
    print("нет")
    
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
