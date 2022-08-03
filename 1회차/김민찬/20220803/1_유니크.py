import sys

sys.stdin = open("1_유니크.txt")

N = int(input())
game = [[], [], []] # 게임 라운드별 참가자들이 제출한 점수 리스트(이차원 리스트)
for i in range(N):
    A, B, C = map(int, input().split())
    game[0].append(A)
    game[1].append(B)
    game[2].append(C)

score = [0] * N # 플레이어 게임 후 누적 점수
for i in range(3):
    for j in range(N):
        if game[i].count(game[i][j]) >= 2: # 같은 수가 2개 이상이면
            score[j] += 0 # 0점
        else:
            score[j] += game[i][j] # 같은 수가 없을 시에 점수 획득

for k in score:
    print(k)