a = int(input())
while a != 0:
    d = 'N'
    x = input()
    for c in range(a):
        if d == 'N' and x[c] == 'D':
            d = 'L'
        elif d == 'N' and x[c] == 'E':
            d = 'O'
        elif d == 'O' and x[c] == 'D':
            d = 'N'
        elif d == 'O' and x[c] == 'E':
            d = 'S'
        elif d == 'L' and x[c] == 'E':
            d = 'N'
        elif d == 'L' and x[c] == 'D':
            d = 'S'
        elif d == 'S' and x[c] == 'E':
            d = 'L'
        elif d == 'S' and x[c] == 'D':
            d = 'O'

    print(d)
    a = int(input())