for c in range(int(input())):
  a = input()
  if ((a[1].isupper()) == True) and (int(a[0])) != (int(a[2])):
    print(int(a[2]) - int(a[0]))
  elif ((a[1].islower()) == True) and (int(a[0])) != (int(a[2])):
    print(int(a[0]) + int(a[2]))
  elif int(a[0]) == int(a[2]):
    print(int(a[0]) * int(a[2]))