while True:
    p = []
    a = int(input())
    if a == 0:
        break
    x = list(map(int, input().split()))
    p = x
    x = sorted(x, reverse=True)
    d = x[1]
    c = p.index(d)
    print(c+1)