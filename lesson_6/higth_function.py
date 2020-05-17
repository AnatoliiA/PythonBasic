from typing import List

my_list = [1, 2, 3, 4, 5, 5, 3, 5]

lambda a, b: a + b

my_list = [1, 2, 3, 4, 5, 5, 3, 5]


def to_square (number):
	return number ** 2


# все значения сохранялся

result = map(to_square, my_list)

print(list(result))
my_list = [1, 2, 3, 4, 5, 5, 3, 5]

result = map(lambda number: number ** 2, my_list)

print(tuple(result))


def get_list ():
	my_list = [1, 2, 34, 5, 6, 7]
	return my_list


result = map(lambda n: n ** 2, get_list())

print(tuple(result))

result = list(map(lambda n: n ** 2, get_list()))

###############FILTER@##########################

new_sequence = [1, 2, 4, 5, 5, 6, 7, 23, 45]
grater_than_50 = []

for number in new_sequence:
	if number > 50:
		grater_than_50.append(number)
print(grater_than_50)


def is_grater_than_50 (number):
	return number > 50


result = filter(is_grater_than_50, new_sequence)
result = filter(lambda n: n > 50, new_sequence)
print(list(result))
# reduce
