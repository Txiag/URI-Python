while True:
    a, b = map(int, input().split())
    x = []
    r = []
    if a == 0 and b == a:
        break
    c = list(map(int, input().split()))
    for i in c:
        if i not in x:
            x.append(i)
        elif (i in x) and (i not in r):
            r.append(i)
    print(len(r))