while True:
    a = int(input())
    p = 0
    if a == 0:
        break
    b = list(map(int, input().split()))
    b.append(b[0])
    b.append(b[1])
    for i in range(1, len(b)-1, 1):
        if (b[i-1] < b[i] and b[i] > b[i+1]) or (b[i-1] > b[i] and b[i+1] > b[i]):
            p += 1
    print(p)
