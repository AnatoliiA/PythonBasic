# We want to change

def test_func ():
	print(' i am outer function')

	def inner_func ():
		print('i am inner function')

	def one_more_innerfunc ():
		print('one more')

	return inner_func, one_more_innerfunc


result = test_func()

# result()
# we can return function by index
test_func()[1]()

# вернуть внутри test_func мы можем только одну функцию?
# а вторыми скобками тогда как выбрать какую из функции мы запустим?
# и можно тогда циклы
# и т.д.
# а вместо индекса срез можно [1:3]?
# то есть кортеж всех функции не запустить?
# сразу
print('+++++++++++++++++++++++++++++++++++++')


def decorator (func):
	def wrapper (arg1):
		# врапер принимает тоже количество елементов что и целевая функцтя
		print('decoration function start')
		result = func(arg1)  # target function print
		print('decoration function ended')
		return result

	# функция декоратор должна возращать врапер
	# функция декоратор должна принимать старт
	return wrapper


# Целевая функция.
@decorator
def start (arg1):
	print('Function has been started')
	return 12


b = start(10)

print(b)


def showdoc (f):
	if f.__doc__:
		print('{}: {}'.format(f.__name__, f.__doc__))
	else:
		print('{}: no docstring!'.format(f.__name__))


@showdoc
def f1 (): """a docstring"""


@showdoc
def f2 (): pass
