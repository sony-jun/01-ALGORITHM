# 채점 상 런타임에러

mushrooms = []

for i in range(10) :
  mushroom = int(input())

  mushrooms.append(mushroom)

sum = 0
near_100 = []

for score in mushrooms :
  sum += score
  near_100.append(sum)

for index in range(len(near_100)) :
  if near_100[index] >= 100 :
    print(near_100[index])
    break

  else :
    if (100 - near_100[index]) < (near_100[index+1] - 100) :
      print(near_100[index])
      break