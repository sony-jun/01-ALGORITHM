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

# 정답 코드

score = []
ans = 0
j = 0

for i in range(10) :
    score.append(int(input()))

while j <= 9 :
    ans += score[j]

    if ans == 100 :
        break

    elif ans > 100 :
        if ans - 100 <= 100 - (ans - score[j]) :
            break
        else :
            ans = ans - score[j]
        break

    j += 1

print(ans)    
