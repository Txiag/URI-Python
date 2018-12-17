a,b, c = map(float, input().split())
if a<c:
    a,c = c,a
if a<b:
    a, b = b,a
if a>= b+c:
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')
if a == b and b == c:
    print('TRIANGULO EQUILATERO')
elif (a==b and b!=c) or (a==c and c != b) or (b==c and c!=a):
    print('TRIANGULO ISOSCELES')
