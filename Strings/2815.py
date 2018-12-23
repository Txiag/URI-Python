a = input().split()
x = []
for i in a:
    if len(i)<4:
      x.append(i)
    elif i[0:2] == i[2:4]:
        x.append(i[2:])
    else:
      x.append(i)
print(*x)
