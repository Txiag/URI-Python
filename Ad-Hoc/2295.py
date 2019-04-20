a = input().split()
c = 0
for c in range(0,len(a)):
    a[c] = float(a[c])
a1 = a[0] / a[2]
a2 = a[1] / a[3]
if a1>a2:
    print('G')
elif a1 == a2:
    print('G')
elif a2>a1:
    print('A')