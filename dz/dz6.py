pallndrome = str(input('введите на прооверку '))

length_pall = len(pallndrome)


def check_revese (str):
	pull = ""
	for a in str:
		pull = a + pull
	if str == pull:
		return True
	else:
		return False


print(check_revese(pallndrome))
