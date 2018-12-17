a = 0
b = 0
c = [0, 0]
for a in range(1,101):
    c[0] = int(input())
    if c[0] > b:
        b = c[0]
        c[1] = a
print(b)
print(c[1])