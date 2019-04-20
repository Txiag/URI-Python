a = input().split()
c = 0
for c in range(0,len(a)):
    a[c] = int(a[c])
a1 = abs(a[0] - a[2])
a2 = abs(a[1] - a[3])
c = abs(a1+a2)
print(c)