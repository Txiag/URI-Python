a = list(map(int, input().split()))
b = sorted(a)
c = sorted(a, reverse=True)
if a == b:
    print('C')
elif a== c:
    print('D')
else:
    print('N')