a = []
b = []
for c in range(int(input())):
	d = int(input())
	if (d in a) == False:
		a.append(d)
	b.append(d)
a.sort()
for i in a:
    print('{} aparece {} vez(es)'.format(i, b.count(i)))