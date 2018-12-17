a = int(input())
c1 = 1
while c1 != (a+1):
    if c1%2 == 0:
        print('{}^2 = {}'.format(c1, c1**2))
    c1 = c1+1