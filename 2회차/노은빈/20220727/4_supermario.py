mu = []    #버섯 점수 리스트
score = 0  #점수 초기화

for i in range(10): #10개의 숫자
    mu.append(int(input()))
for j in mu :
    score += j
    if score >= 100: #점수가 100보다 크면 
        if score - 100 > 100 - (score - j):  #두 값의 절대값 비교
            score -= j
        break
print(score)