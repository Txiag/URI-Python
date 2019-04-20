a = int(input())
if a <= 10:
    total = 7
elif a>10 and a<=30:
    total = 7+((a-10))
elif a>30 and a<=100:
    total = 27 + ((a-30)*2)
elif a>100:
    total = 167 + ((a-100)*5)

print(total)