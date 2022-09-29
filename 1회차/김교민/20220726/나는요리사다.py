total_score=0 #각 참가자가 받은 점수를 합한 값을 저장할 변수
win=0 #참가자 번호
for i in range(5): #참가자 인원 수가 5명
    score=sum(list(map(int, input().split()))) #각 참가자 마다 받은 점수를 합한 값
    if score>total_score: #만약 참가자의 총 점수가 기존 이전 참가자의 총점보다 높은 경우
        total_score=score # 높은 총점으로 바꾸기
        win=i+1 #range가 0부터 시작하기 때문에 +1해준다.
print(win, total_score)