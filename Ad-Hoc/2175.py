ota, bru, ian = map(float, input().split())
if ota < bru and ota < ian:
    print('Otavio')
elif bru < ota and bru < ian:
    print('Bruno')
elif ian < bru and ian<ota:
    print('Ian')
else:
    print('Empate')