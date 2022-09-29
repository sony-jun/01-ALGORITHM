# https://www.acmicpc.net/problem/5533

# 1 <= x <= 100  동일한 수가 없다면 점수, 있으면 점수 없음  진행횟수 3번
# 1줄 n = 행 = 참가자수 / 2줄부터 n개줄에 각 플레이어 제출 점수 3개(열) 공백 구분 입력
# 3번 게임 진행 후 획득 점수

from pprint import pprint
import sys
sys.stdin = open('70_유니크 .txt')

n = int(input())
m = 3
score_ = [list(map(int, input().split())) for _ in range(n)]
score = 0

for i in range(n):
    for j in range(m):
        main = score_[i][j]                     
        # 기준 점수를 메인에 할당
        other = [score_[i][j] for i in range(n)]
        # 1게임은 1열에 있는 점수들을 확인하면 되므로 1열의 점수들을 리스트에 담음
        if other.count(main) == 1:              
        # 기준 점수가 1게임안에 몇개 있는지 카운트(본인점수도 포함이기에 비교값은 1)
            score += main                       
            # 카운트 한 값이 1로 자신 외에 동일 점수가 없으면 score에 점수 누적
    print(score)                                
    # m(열)횟수만큼 반복 하면 1명의 총 게임 점수가 나옴
    score = 0                                  
     # 다음 n(행)으로 가기 전 score는 0으로 초기화
        