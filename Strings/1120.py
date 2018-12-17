while True:
    s = ''
    d, n = input().split()
    if d == '0' and d == n:
        break
    for i in range(len(n)):
        if n[i] != d:
            s += n[i]
    if s == '':
        s = 0
    print(int(s))
