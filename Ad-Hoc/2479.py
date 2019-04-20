a = int(input())
b = []
c = 0
for i in range(a):
  d = input().split()
  b.append((d[1].lower()).capitalize())
  if d[0] == "+":
    c+=1
for i in (sorted(b)):
  print(i)
print("Se comportaram: {} | Nao se comportaram: {}".format(c, abs(c-a)))