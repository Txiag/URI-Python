def qnt(a):
    c = 0
    while a>1:
        a=a/2
        c+=1
    return c
for i in range(int(input())):
    print(qnt(float(input())),'dias')