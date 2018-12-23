for i in range(int(input())):
    a = input()
    if len(a) != 20 or a[0:2] != 'RA':
        print('INVALID DATA')
    else:
        print(int(a[2:]))
