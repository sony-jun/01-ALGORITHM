import sys
from pprint import pprint
sys.stdin = open("1_유니크.txt", 'r')

participants = int(sys.stdin.readline())

scores = []

for _ in range(participants):
    scores.append([*map(int, sys.stdin.readline().split())])

res = []

for _ in range(len(scores)):
    res.append(0) # 각 라운드의 결과를 합산해서 출력할 리스트를 초기화



games = []

for My_score_n in range(3):
    round_ = []
    
    for My_score in range(len(scores)):
        round_.append(scores[My_score][My_score_n]) # N 번째 라운드
    
    round_tmp = list(round_) # N 번째 라운드의 리스트 정보를 담을 임시 리스트
    games.append(round_tmp) # 점수의 변동 사항이 없는 원본 점수정보
    
    for player in range(len(round_)): # 각 라운드의 N 번째 플레이어에 대한 for 문
        if round_.count(round_[player]) >= 2: # round_ 안에 어떤 점수가 여러개 있으면
            games[My_score_n][player] = 0 # 그 점수를 가진 플레이어는 원본 리스트에서 자기 원래점수 대신 0 점으로 바뀜
        res[player] += games[My_score_n][player] # 0 점으로 바뀐 점수 정보를 total 에 적용

for i in range(len(scores)):
    print(res[i])