# Задание 1
print('Введите пароль:')
password = input()
if password == "пароль":
    print('Проходи!')
else:
    print('Доступ запрещен!')

# Задание 2
# Задание 5
fisher1 = int(input())
fisher2 = int(input())

if fisher1 < fisher2:
    print(fisher1)
else:
    print(fisher2)
  
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
