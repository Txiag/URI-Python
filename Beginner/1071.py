a = int(input())
b = int(input())
c = 0
d = 0
if a > b:
    aux = b
    b = a
    a = aux
for c in range(a+1,b):
    if c % 2 != 0:
        d = d + c
print(d)