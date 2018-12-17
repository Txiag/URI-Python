for c in range(0, int(input())):
    a, b = map(int, input().split())
    if b>a:
        a,b = b,a
    while (b != 0):
        d = a % b
        a = b
        b = d
    print(a)
