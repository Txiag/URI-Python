a = int(input())
c = 0
c2 = 0
c1 = 0
for c in range(a):
    c1, c2 = map(int, input().split())
    print('{} cm2'.format(int((c1*c2)/2)))