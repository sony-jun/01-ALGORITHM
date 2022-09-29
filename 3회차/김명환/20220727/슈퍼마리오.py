score_list = [] #입력받을 점수 리스트.
score = 0 # 마리오의 현재 스코어 
# 점수 입력
for i in range(10):
    score_list.append(int(input()))
# 현재 점수에 입력 받은 점수 리스트 첫 요소부터 더해줌 
for i in range(len(score_list)):
    score += score_list[i]
    # 현재 점수가 100점 이상일때.
    if score >= 100:
        # 현재score 에서 100 점을 뺀 경우가(큰 경우) 100 점에서 이전 점수를 뺀 경우보다 클때 // 100에서 보다 더 멀리 있을때  
        if score-100 > 100-(score-score_list[i]):
            score = score-score_list[i]
            break      
        # 현재 스코어가 이전의 점수와 동점이거나 100 점보다 가까이 있을경우 현재 점수 그대로 출력.
        else:
            score = score
            break
print(score)         