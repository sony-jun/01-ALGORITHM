import sys
input = sys.stdin.readline

#참가자 수와 참가자 점수들을 입력한다.
n = int(input())
score_l = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(3):
       score = [score_l[a][j] for a in range(n)]
       score.remove(score_l[i][j])
       
       if score_l[i][j] not in score:
           cnt += score_l[i][j]
           
    print(cnt)