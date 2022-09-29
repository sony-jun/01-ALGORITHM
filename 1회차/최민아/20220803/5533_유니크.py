import sys
sys.stdin = open("20220803/5533_유니크.txt")

N = int(input())                                    # 참가자 수
score = [0] * N                                     # 참가자 점수

game = []                                           # 카드에 적은 수
for i in range(N):                                  # 참가자 별로
    game.append(list(map(int, input().split())))    # 2차원 배열에 저장

for j in range(3):                                  # 3번의 게임
    round = [game[i][j] for i in range(N)]          # 각 라운드별 N명이 카드에 적은 수
    
    for i in range(N):                              # N개의 카드 중에서
        if round.count(round[i]) == 1:              # 각 수의 개수가 1이면
            score[i] += round[i]                    # 겹치지 않으므로 점수 추가

for i in range(N):
    print(score[i])                                 # N명의 총 점수 출력