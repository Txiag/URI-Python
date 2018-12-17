a = int(input())
c = 0
to = 0
ra = 0
co = 0
s = 0
for c in range(1, a+1):
    b = input().split()
    b[0] = int(b[0])
    b[1] = b[1].upper()
    if b[1] == 'C':
        co = co + b[0]
        to = to+ b[0]
    if b[1] == 'R':
        ra = ra + b[0]
        to = to + b[0]
    if b[1] == 'S':
        s = s+b[0]
        to = to+b[0]
print('Total: {} cobaias'.format(to))
print('Total de coelhos: {}'.format(co))
print('Total de ratos: {}'.format(ra))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format((co/to)*100))
print('Percentual de ratos: {:.2f} %'.format((ra/to)*100))
print('Percentual de sapos: {:.2f} %'.format((s/to)*100))
