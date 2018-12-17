a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if (a + b > c) and (c + b > a) and (a + c > b):
    print('Perimetro = {:.1f}'.format(a+b+c))
else:
    print('Area = {:.1f}'.format(((a+b)/2)*c))