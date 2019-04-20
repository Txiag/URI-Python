while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    d = str(a)
    e = int(d[0])
    x = str(b)
    z = int(x[0])
    while len(d) != 1:
        e = int(d[0])
        for c in range(1, len(d)):
            e = e+int(d[c])
        d = str(e)
    while len(x) != 1:
        z = int(x[0])
        for c in range(1, len(x)):
            z= z+int(x[c])
        x = str(z)
    if x==d:
        print('0')
    elif d > x:
        print(1)
    elif x>d:
        print(2)