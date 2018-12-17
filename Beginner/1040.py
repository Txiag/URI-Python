a = input().split()
n1 = (float(a[0])) * 2
n2 = (float(a[1])) * 3
n3 = (float(a[2])) * 4
n4 = float(a[3])
media = (n1+n2+n3+n4)/10
print('Media: {:.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')
if media < 5:
    print('Aluno reprovado.')
if media >=5 and media <= 6.9:
    print('Aluno em exame.')
    nf = float(input())
    print('Nota do exame: {}'.format(nf))
    nf = (nf + media)/2
    if nf >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(nf))
    if nf < 5:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(nf))