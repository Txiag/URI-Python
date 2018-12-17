a = float(input())
if a > 0:
    b = a * 1.15
if a > 400:
    b = a * 1.12
if a > 800:
    b = a * 1.10
if a > 1200:
    b = a * 1.07
if a > 2000:
    b = a * 1.04
print('Novo salario: {:.2f}'.format(b))
print('Reajuste ganho: {:.2f}'.format(b - a))
print('Em percentual: {:.0f} %'.format(((b/a)-1)*100))