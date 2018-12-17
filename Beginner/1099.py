a = int(input())
d = 0
while a != 0:
	b = input().split()
	b[0] = int(b[0])
	b[1] = int(b[1])
	if b[0] > b[1]:
	    aux = b[1]
	    b[1] = b[0]
	    b[0] = aux
	for c in range((b[0]+1),b[1]):
	    if c % 2 != 0:
	        d = d + c
	print(d)
	d=0
	a = a-1