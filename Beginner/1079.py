a = int(input())
c = 0
for c in range(1, a+1):
    b = input().split()
    b[0] = float(b[0])
    b[1] = float(b[1])
    b[2] = float(b[2])
    m = ((b[0] * 2)+(b[1]*3)+(b[2]*5))/10
    print('{:.1f}'.format(m))
    m = 0