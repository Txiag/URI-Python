A = str(input())
A = str.split(A)
B = int(A[1])
C = int(A[2])
D = int(A[3])
A = int(A[0])
if ((B>C) and (D>A) and ((C+D)>(A+B)) and (C>0) and (D>0) and (A%2 == 0)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')