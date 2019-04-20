a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
a[3] = int(a[3])
p1 = a[0] * a[1]
p2 = a[2] * a[3]
if p2 == p1:
    print(0)
elif p1 < p2:
    print(1)
elif p2 < p1:
    print(-1)