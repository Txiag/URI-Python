also = True
while also == True:
    a = input()
    if a == '0+0=0':
        print('True')
        also = False
        a = ''
        exit()
    c1 = len(a)
    if also == True:
        b = ''
        while c1 != -1:
            b = b + a[c1:c1+1]
            c1 = c1-1
        e = int(b[0:b.find('=')])
        d = int(b[b.find('=')+1:b.find('+')])
        f = int(b[b.find('+')+1:])
        if f+d == e:
            print('True')
        elif f+d != e:
            print('False')