a = int(input())
ab = 0
d = []
while a != 0:
    del d[:]
    b = int(input())
    p = 0
    while b != 0:
        c = input().upper()
        if c == 'LEFT':
            p = p - 1
            d.append('p - 1')
        elif c =='RIGHT':
            p = p + 1
            d.append('p + 1')
        else:
            c = int(c[8:])
            if d[c-1] == 'p - 1':
                p = p-1
                d.append('p - 1')
            elif d[c-1] == 'p + 1':
                d.append('p + 1')
                p = p+1
        b = b-1
    print(p)
    a = a-1