mush = []
score = 0

for i in range(10):
    mush.append(int(input())) #점수를 10번 input시킨다.
for j in mush:
    score += j #점수들을 하나씩 더해나간다.
# 점수가 100이상일 경우에 if 조건문으로 진행한다.
    if score >= 100:
    #숫자를 더했을때와 더하지 않았을 때를 비교해 100과 더 가까운 숫자를 구한다.
    #두 경우가 동일하게 가까울 경우에는 최대값으로 한다.
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)