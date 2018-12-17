a = input().split()
b = int(a[1])
c = int(a[2])
a = int(a[0])
a1 = a
b1 = b
c1 = c
if b < a:
    aux = a
    a = b
    b = aux
if c < a:
    aux = a
    a = c
    c = aux
if c < b:
    aux = b
    b = c
    c = aux

print(a)
print(b)
print(c)
print('')
print(a1)
print(b1)
print(c1)