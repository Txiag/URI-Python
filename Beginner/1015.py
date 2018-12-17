x1 = input().split()
x1[0] = float(x1[0])
x1[1] = float (x1[1]) #y1
y1 = input().split()
y1[0] = float(y1[0])  #x2
y1[1] = float (y1[1]) #y2
d = (y1[0] - x1[0])**2 + (y1[1] - x1[1])**2
d = d**0.5
print('{:.4f}'.format(d))