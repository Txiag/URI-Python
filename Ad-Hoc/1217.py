mp = 0
mr = 0
d = 0
for c in range(int(input())):
	d += 1
	p = float(input())
	a = input().split()
	print('day {}: {} kg'.format(d, len(a)))
	mp += p
	mr += len(a)
print('{:.2f} kg by day'.format(mr/d))
print('R$ {:.2f} by day'.format(mp/d))