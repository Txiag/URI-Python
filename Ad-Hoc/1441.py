a = 2
while a != 0:
    b = []
    a = int(input())
    m = a
    if a == 0:
        break
    while a != 1:
        if a % 2 == 0:
            a = a*0.5
            if a > m:
                m = a
        elif a % 2 !=0:
            a = (a * 3)+1
            if a > m:
                m = a
    print(int(m))
