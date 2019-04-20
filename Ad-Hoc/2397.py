a,b, c = map(int, input().split())
if a<c:
    a,c = c,a
if a<b:
    a, b = b,a
if not((abs(b-c) < a and a < b+c) or (abs(a-c) < b and b < a+c) or (abs(a-b) < c and c < a+b)):
    print('n')
elif (a*a) < ((b*b) + (c*c)):
    print('a')
elif (a*a) == ((b*b) + (c*c)):
    print('r')
elif (a*a) > ((b*b) + (c*c)):
    print('o')

