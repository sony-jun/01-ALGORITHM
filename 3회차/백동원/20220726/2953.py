best_score = 0
winner = 0
for a in range(1, 6):                       
    score = list(map(int, input().split())) # 5명의 참가자를 순회하며 입력받는다
    if best_score < sum(score):             # 입력받은 score의 합이 best_score 보다 크다면
        best_score = sum(score)             # 그 값을 best_score에 대입하고
        winner = a                          # 그에 해당하는 참가자 번호도 winner에 대입한다.
print(winner, best_score)                   # 자동으로 제일 큰 점수와 그에 해당하는 참가자번호를 출력할 수 있다.