# Задание 1
def max_consecutive_spaces(text):
    max_count = 0
    current_count = 0

    i = 0
    while i < len(text):
        if text[i] == ' ' or text[i] == '\t' or text[i] == '\n':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
        i += 1

    return max_count

user_text = input("Введите текст: ")
result = max_consecutive_spaces(user_text)
print(f"Максимальное количество последовательных пробельных символов: {result}")

# Задание 2
def max_repeating_chars(text):
    if not text:  # строка пустая
        return 0
    
    max_count = 1  # минимум 1 символ
    current_count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1  # сброс счётчика
    
    return max_count

user_text = input("Введите текст: ")
result = max_repeating_chars(user_text)
print(f"Максимальное число одинаковых символов подряд: {result}")

# Задание 3
def count_unique_letters(text):
    unique_letters = set()
    
    for char in text.lower():
        if char.isalpha():  # проверка (символ — буква)
            unique_letters.add(char)
    
    return len(unique_letters)

user_text = input("Введите текст: ")
result = count_unique_letters(user_text)
print(f"Количество различных букв: {result}")

# Задание 4
def find_char_with_three_occurrences(text):
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        if count == 3:
            return char
    
    return None

user_text = input("Введите текст: ")
result = find_char_with_three_occurrences(user_text)
print(f"Символ, который встречается ровно 3 раза: '{result}'")

# Задание 5
def unique_chars_in_one_string(s1, s2, s3):
    set1 = set(s1)
    set2 = set(s2)
    set3 = set(s3)
    
    # Символы, уникальные для каждой строки
    unique_to_s1 = set1 - set2 - set3
    unique_to_s2 = set2 - set1 - set3
    unique_to_s3 = set3 - set1 - set2
    
    # Объединяем все уникальные символы
    result = unique_to_s1 | unique_to_s2 | unique_to_s3
    
    return sorted(result)

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
str3 = input("Введите третью строку: ")

unique_chars = unique_chars_in_one_string(str1, str2, str3)

print("Символы, встречающиеся только в одной строке:", ', '.join(f"'{c}'" for c in unique_chars))

# Задание 6
sentence = input("Введите предложение: ")  

# Разбиваем на слова, переворачиваем и соединяем обратно
reversed_sentence = ' '.join(sentence.split()[::-1])

print("Предложение в обратном порядке:", reversed_sentence)

# Задание 7 (поиск самого короткого слова)

sentence = input("Введите предложение: ")

words = sentence.split()  # Разбиваем на слова

if not words:  # Проверка на пустой ввод
    print("Предложение не содержит слов!")
else:
    min_length = min(len(word) for word in words)
    print(f"Длина самого короткого слова: {min_length}")

# Задание 8
sentence = input("Введите предложение: ")
words = sentence.split()  # Разбиваем на слова
sorted_words = sorted(words, key=len)

print("Слова в порядке неубывания длин:")
print(' '.join(sorted_words))

# Задание 9
sentence = input("Введите предложение: ")
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    if count == 2:
        print(f"Повторяющееся слово: '{word}'")
        break

# Задание 10
sentence = input("Введите предложение: ")
words = sentence.split()

if not words:
    print("Нет слов в предложении")
else:
    first_word = words[0]  # Запоминаем первое слово
    result_words = []

    for word in words[1:]:  # Проверяем все слова, кроме первого
        if word != first_word and len(word) == len(set(word)):
            result_words.append(word)

    print("Подходящие слова:", ", ".join(result_words))

# Задание 11
cities = input("Введите города через пробел: ").split()

if not cities:
    print("Нет городов")
else:
    winner = None
    for i in range(1, len(cities)):
        prev_city = cities[i-1]
        current_city = cities[i]
        if current_city[0].lower() != prev_city[-1].lower():
            if i % 2 == 1:
                winner = "Петя"
            else:
                winner = "Вася"
            break
    else:
        if len(cities) % 2 == 1:
            winner = "Петя"
        else:
            winner = "Вася"

    print(f"Победитель: {winner}")

# Задание 12
import keyword

def is_valid_python_name(name):
    if not name:
        return False
    
    first_char = name[0]
    if not (first_char.isalpha() or first_char == '_'):
        return False
    
    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False
        
    if keyword.iskeyword(name):
        return False
    
    return True

user_input = input("Введите строку для проверки: ")
if is_valid_python_name(user_input):
    print("Это корректное имя в Python")
else:
    print("Это некорректное имя в Python")

# Задание 13
def is_lucky_ticket(ticket):
    if not ticket.isdigit() or len(ticket) % 2 != 0:
        return False
    
    half = len(ticket) // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    
    # Сумма цифр первой и второй половины
    sum_first = sum(int(d) for d in first_half)
    sum_second = sum(int(d) for d in second_half)
    
    return sum_first == sum_second

# Основная программа
ticket = input("Введите номер билета (или 'стоп' для завершения): ").strip()
position = 1

while ticket.lower() != 'стоп':
    if is_lucky_ticket(ticket):
        print(f"Первый счастливый билет найден на позиции {position}")
        break
    
    ticket = input("Введите следующий номер: ").strip()
    position += 1
else:
    print("Счастливый билет не найден")

# Задание 14
def clear_screen():
    print("\n" * 25)

def display_word(word, guessed_letters):
    displayed = []
    for letter in word:
        if letter in guessed_letters:
            displayed.append(letter)
        else:
            displayed.append('*')
    return ''.join(displayed)

hint = input("Введите подсказку: ")
secret_word = input("Введите загаданное слово: ").lower()

clear_screen()

guessed_letters = set()
attempts = 10
word_guessed = False

print(hint)
print(display_word(secret_word, guessed_letters))

while attempts > 0 and not word_guessed:
    choice = input("Буква или слово (0 - буква, 1 - слово)? ")
    
    if choice == '0':
        letter = input("Введите букву: ").lower()
        if letter in secret_word:
            guessed_letters.add(letter)
            print("Такая буква есть!")
        else:
            attempts -= 1
            print(f"Такой буквы нет! Осталось попыток: {attempts}")
        
        current_display = display_word(secret_word, guessed_letters)
        print(current_display)
        
        if '*' not in current_display:
            word_guessed = True
    
    elif choice == '1':
        guess = input("Введите слово: ").lower()
        if guess == secret_word:
            word_guessed = True
        else:
            attempts -= 1
            print(f"Неверно! Осталось попыток: {attempts}")
            print(display_word(secret_word, guessed_letters))
    
    else:
        print("Некорректный ввод. Введите 0 или 1.")

if word_guessed:
    print("Победа!")
else:
    print("Проигрыш!")
    print(f"Загаданное слово было: {secret_word}")

# Задание 15
def clear_screen():
    print("\n" * 25)

def get_secret_number():
    while True:
        num = input("Ведущий, введите 4-значное число с неповторяющимися цифрами: ")
        if len(num) == 4 and num.isdigit() and len(set(num)) == 4:
            return num
        print("Некорректный ввод! Число должно быть 4-значным с неповторяющимися цифрами.")

def count_bulls_and_cows(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

# Основная часть программы
secret_number = get_secret_number()
clear_screen()

attempts = 10
print("У вас 10 попыток отгадать 4-значное число с неповторяющимися цифрами.")

while attempts > 0:
    guess = input(f"Попытка {11 - attempts}. Введите ваше число: ")
    
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        print("Некорректный ввод! Нужно 4-значное число с неповторяющимися цифрами.")
        continue
    
    if guess == secret_number:
        print("Быков: 4 Коров: 0")
        print("Победа!")
        break
    
    bulls, cows = count_bulls_and_cows(secret_number, guess)
    print(f"Быков: {bulls} Коров: {cows}")
    attempts -= 1
else:
    print("Проигрыш!")
    print(f"Загаданное число было: {secret_number}")

# Задание 16
def is_brackets_balanced(text):
    balance = 0
    for char in text:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:  # Закрывающая скобка без открывающей
                return False
    return balance == 0

text = input("Введите текст: ")
if is_brackets_balanced(text):
    print("Скобки расставлены правильно!")
else:
    print("Ошибка в расстановке скобок!")

# Задание 17
def calculate(expression):
    # удаляем пробелы
    expr = expression.replace(" ", "")
    
    def evaluate(expr):
        numbers = []
        operators = []
        i = 0
        while i < len(expr):
            if expr[i] == '(':
                # вычисляем выражение в скобках
                j = i + 1
                balance = 1
                while j < len(expr) and balance != 0:
                    if expr[j] == '(':
                        balance += 1
                    elif expr[j] == ')':
                        balance -= 1
                    j += 1
                num = evaluate(expr[i+1:j-1])
                numbers.append(num)
                i = j
            elif expr[i].isdigit():
                # Считываем число целиком
                j = i
                while j < len(expr) and expr[j].isdigit():
                    j += 1
                num = int(expr[i:j])
                numbers.append(num)
                i = j
            else:
                # Добавляем оператор
                operators.append(expr[i])
                i += 1
        
        i = 0
        while i < len(operators):
            op = operators[i]
            if op in '*/':
                a = numbers[i]
                b = numbers[i+1]
                if op == '*':
                    numbers[i] = a * b
                else:
                    numbers[i] = a // b
                del numbers[i+1]
                del operators[i]
                i -= 1
            i += 1
        
        result = numbers[0]
        for i in range(len(operators)):
            op = operators[i]
            num = numbers[i+1]
            if op == '+':
                result += num
            else:
                result -= num
        
        return result
    
    return evaluate(expr)

expression = input("Введите арифметическое выражение: ")
print("Результат:", calculate(expression))

# Задание 18
def justify_text(text, width):
    words = text.split()
    if not words:
        return ""
    
    lines = []
    current_line = []
    current_length = 0
    
    # Формируем строки
    for word in words:
        # Проверяем, помещается ли слово в текущую строку
        if current_line:
            # Учитываем пробел перед словом
            if current_length + 1 + len(word) <= width:
                current_line.append(word)
                current_length += 1 + len(word)
            else:
                lines.append(current_line)
                current_line = [word]
                current_length = len(word)
        else:
            current_line.append(word)
            current_length = len(word)
    
    if current_line:
        lines.append(current_line)
    
    # Выравниваем строки (кроме последней)
    justified_lines = []
    for i in range(len(lines) - 1):
        line = lines[i]
        if len(line) == 1:
            justified_lines.append(line[0].ljust(width))
        else:
            total_spaces = width - sum(len(word) for word in line)
            gaps = len(line) - 1
            base_space = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            
            justified_line = []
            for j in range(gaps):
                justified_line.append(line[j])
                justified_line.append(' ' * (base_space + (1 if j < extra_spaces else 0)))
            justified_line.append(line[-1])
            
            justified_lines.append(''.join(justified_line))
    
    # Последняя строка - выравнивание по левому краю
    last_line = ' '.join(lines[-1]) if lines else ""
    justified_lines.append(last_line.ljust(width))
    
    return '\n'.join(justified_lines)

text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))
print(justify_text(text, width))

# Задание 19
def can_divide_word(word, pos):
    """Проверяет, можно ли разделить слово в указанной позиции"""
    vowels = "аеёиоуыэюя"
    # Не переносим слишком короткие слова
    if len(word) < 4 or pos < 2 or pos > len(word)-2:
        return False
    # Перенос после гласной
    if word[pos-1].lower() in vowels:
        return True
    # Перенос между слогами (упрощённо)
    if word[pos-1].lower() not in vowels and word[pos].lower() in vowels:
        return True
    return False

def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        while True:
            # Проверяем, помещается ли слово (или часть слова)
            line_len = sum(len(w) for w in current_line) + len(current_line) - 1
            space_left = width - line_len - 1  # -1 для пробела
            
            if len(word) <= space_left:
                current_line.append(word)
                break
            else:
                # Пытаемся перенести часть слова
                for pos in range(min(space_left-1, len(word)-1), 0, -1):
                    if can_divide_word(word, pos):
                        part1 = word[:pos] + '-'
                        part2 = word[pos:]
                        current_line.append(part1)
                        lines.append(' '.join(current_line))
                        current_line = []
                        word = part2
                        break
                else:
                    # Не смогли перенести - новая строка
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]
                    break
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Выравниваем строки по ширине
    result = []
    for i, line in enumerate(lines):
        words_in_line = line.split()
        if i == len(lines)-1 or len(words_in_line) == 1:
            result.append(line.ljust(width))
        else:
            spaces = width - sum(len(w) for w in words_in_line)
            gaps = len(words_in_line) - 1
            base, extra = divmod(spaces, gaps)
            line_parts = []
            for j in range(gaps):
                line_parts.append(words_in_line[j] + ' '*(base + (1 if j < extra else 0)))
            line_parts.append(words_in_line[-1])
            result.append(''.join(line_parts))
    
    return '\n'.join(result)

# Ввод данных
text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))

# Обработка и вывод
print("\nРезультат:\n" + justify_text(text, width))

# Задание 20
def num_to_words(n):
    if n == 0: return "ноль"
    
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
            "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", 
           "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
               "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    
    def convert_part(num, gender):
        res = []
        if num >= 100:
            res.append(hundreds[num // 100])
            num %= 100
        if num >= 20:
            res.append(tens[num // 10])
            num %= 10
        if 10 <= num < 20:
            res.append(teens[num - 10])
        elif num > 0:
            if gender == 'f' and num in (1, 2):
                res.append(["одна", "две"][num-1])
            else:
                res.append(units[num])
        return ' '.join(res)
    
    result = []
    if n >= 1_000_000:
        million_part = n // 1_000_000
        result.append(convert_part(million_part, 'm'))
        result.append("миллион" + ("а" if 2 <= million_part % 10 <= 4 and million_part % 100 not in (12,13,14) else 
                       "ов" if million_part % 10 != 1 or million_part % 100 == 11 else ""))
        n %= 1_000_000
    
    if n >= 1000:
        thousand_part = n // 1000
        result.append(convert_part(thousand_part, 'f'))
        result.append("тысяч" + ("а" if thousand_part % 10 == 1 and thousand_part % 100 != 11 else 
                       "и" if 2 <= thousand_part % 10 <= 4 and thousand_part % 100 not in (12,13,14) else ""))
        n %= 1000
    
    if n > 0:
        result.append(convert_part(n, 'm'))
    
    return ' '.join(result).strip()

num = int(input("Введите число (0-900000000): "))
print(num_to_words(num))
