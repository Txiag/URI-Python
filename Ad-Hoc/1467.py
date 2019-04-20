while True:
    try:
        a = input().split()
        if a[0] == a[1] and a[0] != a[2]:
            print('C')
        elif a[0] == a[2] and a[0] != a[1]:
            print('B')
        elif a[1] == a[2] and a[1] != a[0]:
            print('A')
        else:
            print('*')
    except EOFError:
        break