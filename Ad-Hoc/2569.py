def oi(texto):
    texto = str(texto)
    x = ''
    for i in texto:
        if i == '7':
            x += '0'
        else: x+=i
    return x

a = input()
if '+' in a:
    a = a.split('+')
    a[0] = oi(a[0])
    a[1] = oi(a[1])
    a = oi(str(int(a[0]) + int(a[1])))
elif '-' in a:
    a = a.split('-')
    a[0] = oi(a[0])
    a[1] = oi(a[1])
    a = oi(int(a[0]) - int(a[1]))
elif 'x' in a.lower():
    a = a.split('x')
    a[0] = oi(a[0])
    a[1] = oi(a[1])
    a = oi(int(a[0]) * int(a[1]))
else:
    a = a.split('/')
    a[0] = oi(a[0])
    a[1] = oi(a[1])
    a = oi(int(a[0]) / int(a[1]))
print(int(a))