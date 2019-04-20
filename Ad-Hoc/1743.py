a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = True
for i in range(len(b)):
    if a[i] == b[i]:
        d = False
        break
if d == True:
    print('Y')
else:
    print('N')