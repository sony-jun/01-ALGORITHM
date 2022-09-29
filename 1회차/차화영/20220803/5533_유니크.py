import sys
input = sys.stdin.readline

N = int(input())
score = [0] * N # N을 곱하지 않았더니 런타임에러가 났음
card = [] # 카드에 적은 수

for i in range(N): # N명의 참가자
    card.append(list(map(int, input().split()))) # 2차원 배열에 저장
for j in range(3): # 3번의 플레이
    row_ = [card[i][j] for i in range(N)] # N명이 한 번의 플레이당 카드에 적은 수

    for i in range(N): # N개의 숫자 중
        if row_.count(row_[i]) == 1: # 행의 각 요소의 개수가 1이면
            score[i] += row_[i] # 행의 요소가 점수가 되는 것임 -- 점수 = [0, 0, 0, 0, 0]의 리스트 형태이므로 '점수[i]'에 더해야 5명 3번 플레이 총점 구할 수 있다!

for i in range(N):
    print(score[i])