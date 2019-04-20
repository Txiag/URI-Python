while True:
	a = input().lower().split()
	if a[0] == '*':
		break
	l = a[0][0]
	x = True
	for i in range(len(a)):
		if a[i][0] != l:
			x = False
	if x == True:
		print('Y')
	else:
		print('N')