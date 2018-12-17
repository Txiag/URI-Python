c=0
c1 = 0
c2 = 0
while c != 6:
    a = float(input())
    if a > 0:
        c1 = c1 + 1
        c2 = c2 + a
    c = c + 1
print('{} valores positivos'.format(c1))
print(round(c2/c1, 1))
