import random, time, math

pasword_list = 'aqwsedrftgtyhyhyujukikilililolololnvbhdb'


def psw (i):
	word = ''
	while (i >= 0):
		word += pasword_list[random.randint(0, len(pasword_list) - 1)]
		i -= 1
	return word + '\n'


file = open('pasword.txt', 'a')
parol_num = int(input('Введите длинну пароля'))
file.write(psw(parol_num))

pallndrome = str(input('введите на прооверку слова на паллиндром'))

length_pall = len(pallndrome)


def check_revese (str):
	pull = ""
	for a in str:
		pull = a + pull
	if str == pull:
		return True
	else:
		return False


print(' это паллиндром?  ответ', check_revese(pallndrome))

words = str(input('введете не менее трех слов резделенных пробелом'))

words_list = words.split()

d = list(map(lambda a: len(a), words_list))

max_w = max(d)

print(len(d), max_w)


def bigword (wrd):
	w = []
	for x in wrd:
		if len(x) == max_w:
			w.append(x)
	return w


result = bigword(words_list)

if len(result) > 1:
	for x in result:
		print(f'вы ввели несколько одинаковых слов {x}')
else:
	print(f'наибольшие слово {result[0]}')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# home assignment !!!!!!!!!!!!!!!!!

# Quiz number one !!!

def decorator (func):
	logs = open('logx.txt', 'a', encoding='utf-8')

	def wrapper ():
		data_strict = time.localtime()
		formatted = time.strftime('Begining  %d %m %Y %X', data_strict)
		# form_d = time.struct_time()
		logs.write('попытка выполнения \t\n')
		logs.write('начало выполение {} \n'.format(formatted))
		f = func()
		logs.write(' result выполение {} \n'.format(f))
		logs.write('начало выполение {} \n'.format(formatted))
		print('I am in wrapper ')

	return wrapper


@decorator
def start ():
	print('I am start ')
	return 'result function '


start()

# Quiz number two
# !!!!!!!!!!!!!!!!@@@@@@@@@@@

rnd = random.randint(1, 100)
td = list(range(rnd))

for x in range(rnd):
	td[x] = random.randint(1, 100)


def sqmap (num):
	if num % 2 == 0:
		return int(math.sqrt(num) * 100) / 100
	else:
		return int(math.sqrt(num) * 100) / 100


xlst = list(map(sqmap, td))
xlst.sort()
print(xlst)


def quickselect (l, k, pivot_fn):
	if len(l) == 1:
		return l[0]

	pivot = pivot_fn(l)

	lows = list(filter(lambda xx: xx < pivot, l))
	highs = list(filter(lambda xx: xx > pivot, l))
	pivots = list(filter(lambda xx: xx == pivot, l))

	if k < len(lows):
		return quickselect(lows, k, pivot_fn)
	elif k < len(lows) + len(pivots):
		return pivots[0]
	else:
		return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def quickselect_median (l, pivot_fn=random.choice):
	if len(l) % 2 == 1:
		return quickselect(l, len(l) / 2, pivot_fn)
	else:
		return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) + quickselect(l, len(l) / 2, pivot_fn))


madiana = quickselect_median(xlst)
print('значения выше медианы {}'.format(madiana, ))
print(list(filter(lambda x: x > madiana, xlst)))

# List of question
# Декораторы:
# почему я не вернул результат wrapper в примере где перевхватівается этот возврат и где вызывается
# Time временной кортеж является екземпляром strict_teme к его єлементам можно обращатся как х.tm_year et setera
# Как это использовать
# formatted = time.strftime('Begining  %d %m %Y %X', data_strict) если добавить к строке в середине время проиходит ощибка
# Для решения задачи использовал учебник по Рафгарден Тим
# Р26 Совершенный алгоритм. Основы. как сделать проще
