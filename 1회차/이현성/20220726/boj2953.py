score_sum = [] # 점수의 합을 모아놓을 리스트

for i in range(5): # 5번 반복
    list_ = list(map(int, input().split())) # input값을 공백으로 나누어 int로 변환해서 리스트에 추가
    score_sum.append(sum(list_)) # 합을 모을 리스트에 추가한다 무엇을? 리스트의 합을
    
print((score_sum.index(max(score_sum))) + 1, max(score_sum))
# print(f'{(score_sum.index(max(score_sum))) + 1} {max(score_sum)}')
# 합을 모아놓은 리스트에서 제일 큰 수가 있는 자리(파이썬은 0부터 시작이기에 자리를 구한후 + 1)
# 그리고
# 합을 모아놓은 리스트에서 제일 큰 수