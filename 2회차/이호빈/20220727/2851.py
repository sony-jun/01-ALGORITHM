m = []
score = 0
for i in range(10):
    m.append(int(input()))
for num in m: # 입력된 값을 리스트에 넣어준 것을 돌으면서
    score += num # 리스트의 값들을 차례대로 score에 넣어주고 
    if score >= 100: # 100보다 크면
        if score - 100 > 100 - (score - num): # 큰 값을 선택해야 하기 위해 서로 비교해준다
            score -= num # 100을 초과한 값에서 초과하기 전의 값을 넣어준다 
        break
print(score)