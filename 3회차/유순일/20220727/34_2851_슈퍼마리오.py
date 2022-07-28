score =[]
ans = 0
j = 0

for i in range(10):
    score.append(int(input()))      # 버섯 10개 값 넣는거.
while j <= 9:
    ans += score[j]
    
    if (ans == 100):    # 점수가 100과 동일하다면 즉시 반복문을 탈출.
        break
    elif (ans > 100):
        if ans - 100 <= 100 - (ans - score[j]):
            break
        else:
            ans = ans - score[j]
        break
    j += 1
print(ans)
