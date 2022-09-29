# https://www.acmicpc.net/problem/5533
# 문제5533번.유니크
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 참가자의 수 N
- 2 <= N <= 200
2. N개의 줄에는 각 플레이어가 첫번째, 두번째, 세번째 게임에서 쓴 수가 주어짐
- 1 <= 정수 <= 100
'''



# 출력
'''
1. 각 플레이어가 3번의 게임에서 얻은 총 점수를 출력
- 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻음
'''



# 코드
import sys

sys.stdin = open('input_text/5533.txt')

# 행렬 생성
N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]

# 3번의 경기동안 각 플레이어가 받게 되는 총점수 구하기
players = [0] * N   # 인덱스: 각 플레이어, 값: 각 플레이어의 총 점수
for c in range(3):   # 3번의 경기
    # 각 경기에서 N명의 플레이어가 쓴 점수들 기록
    scores = []   
    for r in range(N):   # N명의 플레이어
        score = cards[r][c]
        scores.append(score)

    # 자신과 같은 수를 쓴 사람이 없다면 점수를 더함
    for p in range(len(scores)):
        score = scores[p]   # 해당 플레이어가 쓴 점수
        if scores.count(score) == 1:
            players[p] += score

for tot_score in players:
    print(tot_score)
    
            


# 실행결과(메모리:30840KB, 시간:76ms)