while True:
    try:
        c=0
        a,b = map(int, input().split())
        for i in range(a, b+1):
            xx = list(str(i))
            d = True
            for i1 in xx:
                if xx.count(i1) > 1:
                    d = False
                    break
            if d == True:
                c+=1
        print(c)
    except EOFError:
        break
