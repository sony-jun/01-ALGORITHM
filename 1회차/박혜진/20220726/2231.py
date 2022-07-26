bunhae = int(input())

for i in range(bunhae) :
  
  a = sum(map(int, str(i)))
  num = i + a

  if num == bunhae :
    print(i)
    break

else : 
  print(0)