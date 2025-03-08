# Задание 1
print('Введите пароль:')
password = input()
if password == "пароль":
    print('Проходи!')
else:
    print('Доступ запрещен!')

# Задание 2
print('Какие два слова передал первой радиограммой Александр Попов?')
word1 = input('Первое слово: ')
word2 = input('Второе слово: ')
if word1 == 'Генрих' and word2 == 'Герц':
    print('Верно')
else:
    print('Неверно')

# Задание 3
print('Как зовут главного персонажа романов Яна Флеминга о вымышленном шпионе секретной разведывательной службы Великобритании?')
name = input('Имя персонажа: ')
if name.lower() == 'джеймс бонд' or name.lower() == 'агент 007':
    print('Верно')
else:
    print('Неверно')
    
# Задание 5
fisher1 = int(input())
fisher2 = int(input())

if fisher1 < fisher2:
    print(fisher1)
else:
    print(fisher2)

# Задание 8
computer_age = 78
print('Здравствуйте! Как Вас зовут?')
name = input()
print('Очень приятно, ' + str(name) + '! Меня зовут Марк.')
print('Сколько Вам лет?')
human_age = int(input())

if human_age < computer_age:
    difference = computer_age - human_age
else:
    difference = human_age - computer_age

if human_age < computer_age:
    print('Да, ' + str(name) + ', я старше Вас на ' + str(difference) + ' лет.')
else:
    print('Да, ' + str(name) + ', Вы старше меня на ' + str(difference) + ' лет.')

print('Вам нравится программировать?')
like = input()
if like == 'Да' or like == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
else:
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')
    
# Задание 9
print('Собака короткошерстной породы?')
wool = input()


if (wool == 'да'):
    print('Рост собаки менее 50 см?')
    height50 = input()
    if height50 == 'да':
        print('У собаки короткий хвост?')
        tail = input()
        if tail == 'да':
            print('английский бульдог')
        else:
            print('У собаки длинные уши?')
            ears = input()
            if ears == 'да':
                print('гончая')
            else:
                print('У собаки короткое тело?')
                body = input()
                if body == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        print('Собака весит более 50 кг?')
        weight50 = input()
        if weight50 == 'да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    print('Рост собаки менее 50 см?')
    height50 = input()
    if height50 == 'да':
        print('У собаки доброжелательный характер?')
        character = input()
        if character == 'да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        print('У собаки рост менее 70 см?')
        height70 = input()
        if height70 == 'да':
            print('У собаки длинные уши?')
            ears = input()
            if ears == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            print('Окрас рыжий с белыми отметками?')
            orangecolor = input()
            if orangecolor == 'да':
                print('сенбернар')
            else:
                print('Белоснежный окрас?')
                whitecolor = input()
                if whitecolor == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
                    
# Задание 10
print('Могут ли вращаться шестеренки из механизма?')
n_shesterenok = int(input("Укажите количество шестеренок в механизме: "))
if n_shesterenok % 2 == 0:
    print('да')
else:
    print('нет')
