c = 0
d = 0
while d <= 9:
    for c in range (0, 3):
        print('I={}'.format(d+1) , end='')
        print(' J={}'.format(7 - c))
    d = d + 2