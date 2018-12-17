a = int(0)
vp = 0
vn = 0
while a != 5:
    c = int(input())
    if c < 0:
        vn = vn + 1
    if c%2 == 0:
        vp = vp + 1
    a = a+1
print('{} valor(es) par(es)'.format(vp))
print('{} valor(es) impar(es)'.format(5 - vp))
print('{} valor(es) positivo(s)'.format(4 - vn))
print('{} valor(es) negativo(s)'.format(vn))