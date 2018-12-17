a = input().lower()
if a == 'vertebrado':
    a = input().lower()
    if a == 'ave':
        a = input().lower()
        if a == 'carnivoro':
            print('aguia')
        if a == 'onivoro':
            print('pomba')
    elif a == 'mamifero':
        a = input().lower()
        if a == 'onivoro':
            print('homem')
        if a == 'herbivoro':
            print('vaca')
elif a == 'invertebrado':
    a = input().lower()
    if a == 'inseto':
        a = input().lower()
        if a == 'hematofago':
            print('pulga')
        if a == 'herbivoro':
            print('lagarta')
    elif a == 'anelideo':
        a = input().lower()
        if a == 'hematofago':
            print('sanguessuga')
        if a == 'onivoro':
            print('minhoca')