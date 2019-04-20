input()
a = list(map(int, input().split()))
input()
for i in list(map(int,input().split())):
    if i in a:
        del a[a.index(i)]
print(*a)