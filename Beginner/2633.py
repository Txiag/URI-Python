while True:
try:
    a = []
    for i in range(int(input())):
        n, m = input().split()
        x = [int(m), [n]]
        a.append(x)
    a.sort()
    for i in range(len(a)-1):
        print(a[i][1][0], end=' ')
    print(a[len(a)-1][1][0])
except EOFError:
    break
