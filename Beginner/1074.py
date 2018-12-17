c = int(input())
c1 = 0
while c1 != c:
    a = int(input())
    if a > 0:
        if a%2 == 0:
            print('EVEN POSITIVE')
        elif a%2 != 0:
            print('ODD POSITIVE')
    if a < 0:
        if a%2 == 0:
            print('EVEN NEGATIVE')
        elif a%2 != 0:
            print('ODD NEGATIVE')
    if a == 0:
        print('NULL')
    c1 = c1+1