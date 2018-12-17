A = input().split()
B = int(A[1])
A = int(A[0])
if A > B:
    aux = B
    B = A
    A = aux
if (B%A == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')