for c in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    b = list(set(b))
    print(len(b))