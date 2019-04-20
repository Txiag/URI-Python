a = input().split()
x = ''
for i in range(len(a)):
    for c in range(1, len(a[i]), 2):
        x += a[i][c]
    x+= ' '
print(x[0:len(x)-1], end='\n')