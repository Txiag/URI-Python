while True:
    x = 0
    h1,m1,h2,m2 = map(int, input().split())
    if h1 == 0 and m1 == h1 and h2 == m1 and h2 == m2:
        break
    if h1 > h2:
        t1 = h1*60+m1
        t2 = h2*60+m2
        tf = abs(t1-t2)
        tf = 1440 - tf
        x = tf
    elif h2 > h1:
        t1 = h1*60+m1
        t2 = h2*60+m2
        tf = abs(t1-t2)
        x = tf
    elif h1 == h2:
        if m1 == m2:
            x = 1440
        elif m1 > m2:
            x = (1440-(m1-m2))
        elif m2 > m1:
            x = (m2-m1)
    print(x)
