a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = a+b+(abs(a-b))
d = d/2
d = d+c+(abs(d-c))
d = d/2
d = int(d)
print('{} eh o maior'.format(d))