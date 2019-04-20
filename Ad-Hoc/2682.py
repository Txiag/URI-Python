a = 0
b = 0
a = int(input())
b = a
c = 0
d = False
while True:
    try:
        a = int(input())
        if a < b and d == False:
            b = b
            d = True
        elif a>b and d == False:
            b = a
    except EOFError:
        break
print(b+1)