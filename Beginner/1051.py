a = float(input())
if a > 2000 and a < 3000.01:
    t = (a-2000)*0.08
    print('R$ {:.2f}'.format(t))
if a<=2000:
    print('Isento')
if a >= 3000.01 and a <= 4500:
    a = a - 2000
    t = a - 1000
    a = a - t
    a = a *0.08
    t = t*0.18
    t = t + a
    print('R$ {:.2f}'.format(t))
if a > 4500:
    t1 = (a - 4500) * 0.28
    t2 = 1500 * 0.18
    t3 = 1000*0.08
    t = t1+t2+t3
    print('R$ {:.2f}'.format(t))