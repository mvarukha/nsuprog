# Задание 1
all = int(input(''))
print(f'{((all-4608)/6):.0f}')

# Задание 2
country = input()
print(country.replace(' ', '\n'))

# Задание 3
price = input()
print(eval(price.replace(' ', '+')))

# Задание 4
kittens = 7*7*7*7
cats = 7*7*7
bags = 7*7
wifes = 2
print(kittens + cats + wifes + 2)

# Задание 5
print(f'{(int(input())*0.19):.2f}')

# Задание 6
weigth = int(input())
height = int(input())/100
print(f'{(weigth/height**2):.2f}')

# Задание 7
print(str(1000) + 'литров')

# Задание 8
n, m = input().split()
n = int(n)
m = int(m)
print(f'{m//(n+1)}')

# Задание 9
n = int(input())
k = int(input())
print(n%k)

# Задание 10
meters = int(input())
print(f'{(meters/1609.34):.0f}')
