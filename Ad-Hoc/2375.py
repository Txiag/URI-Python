a = int(input())
b = input().split()
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
if a <= b[0] and a<=b[1] and a<=b[2]:
    print('S')
else:
    print('N')