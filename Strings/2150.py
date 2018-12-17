while True:
try:
    a = input()
    b = list(input())
    c = 0
    for i in b:
        if i in a:
            c+=1
    print(c)
except EOFError:
    break