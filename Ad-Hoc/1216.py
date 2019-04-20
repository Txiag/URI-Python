a = []
b = 0
c = 0
while True:
    try:
        d = input()
        a.append(int(input()))
    except EOFError:
        break
for c in range(0, len(a)):
    b = b+int(a[c])
print('{:.1f}'.format(b/len(a)))