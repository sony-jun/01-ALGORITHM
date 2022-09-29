N = int(input())

if (N % 100 != 0 or N % 400 == 0) and N % 4 == 0 :
  print(1)
else:
  print(0)
