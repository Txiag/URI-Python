a = 0
b = []
c = 0
d = False
t = 0
while True:
    try:
        while d == False:
            e,x = input().split()
            for a in range(1, int(e)+1):
                b.append(int(x[a-1:a]))
            for a in range(0, len(b)):
                t = t+b[a]
            c = t/3
            if c.is_integer() == True:
                print('{} sim'.format(t))
            else:
                print('{} nao'.format(t))
            c = 0
            t = 0
            del b[:]
    except EOFError:
        break