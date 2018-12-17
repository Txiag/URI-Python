a = int(input())
b = a
d = 0
c1 = 0
c2 = 0
while b != 0:
    d = int(input())
    if d >=10 and d <= 20:
        c1 = c1+1
    else:
        c2 = c2 + 1
    b = b-1
print('{} in'.format(c1))
print('{} out'.format(c2))
