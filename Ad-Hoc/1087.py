x1, y1, x2, y2 = map(int, input().split())
while not(x1 == 0 and y1 == x1 and x2 == y2 and x1 == x2):
    if x1 == x2 and y1 == y2:
        print(0)
    elif x1 == x2 or y1 == y2 or x1+y1 == x2+y2 or x1-y1 == x2-y2:
        print(1)
    else:
        print(2)
    x1, y1, x2, y2 = map(int, input().split())
