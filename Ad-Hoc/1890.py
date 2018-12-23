def tuk (a, b):
    if a != 0 and b != 0:
        c = 26**a * 10**b
    elif a == 0 and b!= 0:
        c = 10**b
    elif b == 0 and a != 0:
        c = 26**a
    else:
        c = 0

    return c

for i in range(int(input())):
    c, d = map(int, input().split())
    print(tuk(c, d))
