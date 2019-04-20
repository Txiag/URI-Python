a = 1
b = 0
d = 0
e = 0

c = 0
while a != 0:
  a = int(input())
  if a == 0:
    break
  p1 = 0
  p2 = 0
  for c in range(0, a):
    d, e = map(int, input().split())
    if d > e:
      p1 = p1+1
    elif e>d:
      p2 = p2+1
  print(p1, p2)
