while True:
	p = []
	a = int(input())
	if a == 0:
		break
	for i in range(a):
		a = input().split()
		p.append(a)
	m = int(p[0][1]) - int(p[0][2])
	n = p[0][0]
	for i in range(1, len(p)):
		if int(p[i][1]) - int(p[i][2]) < m:
			m = int(p[i][1]) - int(p[i][2])
			n = p[i][0]
	print(n)