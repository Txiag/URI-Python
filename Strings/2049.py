i = 0
while True:
    i+=1
    a = input()
    if a == '0':
        break
    b = input()
    if i > 1:
        print()
    print('Instancia', i)
    if a in b:
        print('verdadeira')
    else:
        print('falsa')
