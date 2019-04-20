while True:
    try:
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        d = []
        if a == b:
            print('*')
        else:
            for i in range(1, a+1):
                if (i in c) == False:
                    d.append(i)
            print(*d, end='')
            print(' ')
    except EOFError:
        break