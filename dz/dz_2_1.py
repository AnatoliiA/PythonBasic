import os, sys

print('задача №1')
print('')
even_number = 2
# even_number = int(input('введите число'))

if even_number % 2 == 0:
	print(f'число {even_number} четное')
else:
	print(f'число {even_number} не четное')

print('')

print('задача №2')
print('')

# base = int(input('введите основание треугольника:'))

# height = int(input('введите height треугольника:'))

# print(f'height of triangle is {base * height / 2}')

print('')

print('задача №3')
myhost = sys.platform
# why do not comment kirilic
# why does not comment

print(f'операционная система {os.name}')
print(f'количество ядер в системе {os.cpu_count()}')
print('платформа :', myhost)

print('')

metr = int(input('введите количество метров'))
convert = int(input('введите во что конвертировать метры 1 мм 2 см 3 км'))
if convert == 1:
	print(f'{metr} это {metr * 1000} мм')
elif convert == 2:
	print(f'{metr} это {metr * 100} см')
elif convert == 2:
	print(f'{metr} это  {metr / 1000} км')
else:
	print('ввели не правильное число')

print('задача №5')
list_int = [1, 4, 5, 6, 12]
i = len(list_int) - 1
h = 0
while i >= 0:
	h += list_int[i]
	i -= 1

print(h)
