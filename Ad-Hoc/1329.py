m = 0
j = 0
c = ''
while True:
    m = 0
    j = 0
    d = input()
    if d == '0':
        break
    c = input()
    c = c.split()
    for d in range(0, len(c)):
        if c[d] == '0':
            m = m+1
        if c[d] == '1':
            j = j+1
    print('Mary won {} times and John won {} times'.format(m, j))