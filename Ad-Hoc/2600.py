for i in range(int(input())):
  a = int(input())
  b = list(map(int, input().split()))
  c = int(input())
  ver = ""
  for i in b:
    ver += str(i)
  ver += str(a)
  ver += str(c)
  ver = "".join(sorted(list(ver)))
  if a + c == 7 and b[0] + b[2] == 7 and b[1] + b[3] == 7 and ver == "123456":
      print("SIM")
  else:
      print("NAO")