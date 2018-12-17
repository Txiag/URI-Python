a = input().split()
b = int(a[1])
a = int(a[0])
if b > a:
    print('O JOGO DUROU {} HORA(S)'.format(((b - a))))
else:
    print('O JOGO DUROU {} HORA(S)'.format(((a-24)-b)*-1))