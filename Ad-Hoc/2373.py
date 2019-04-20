ans = 0
for i in range(int(input())):
    l, c = map(int, input().split())
    if l>c:
        ans += c
print(ans)