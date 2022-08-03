import sys

sys.stdin = open("5533.txt", "r")

N = int(input()) # 플레이어 수 입력받기

score = [0] * N # 플레이어들의 총 점수 입력(0으로 초기화)
matrix = [list(map(int, input().split())) for _ in range(N)] # 컴프리헨션으로 입력값 2차원 배열로 받기

for i in range(3): # 3게임을 하면서 한 게임당 세로줄이 [][i]로 되는 것을 사용
    for j in range(N): # 특정 플레이어를 기준으로 비교한다
        for k in range(N): # 다른 플레이어들 비교
            check = matrix[j][i] # 특정 플레이어가 작성한 값
            if j == k: # 같은 자리에 있는 플레이어를 비교할 경우 continue
                continue
            if matrix[j][i] == matrix[k][i]: # 같은 값을 작성한 플레이어가 존재할 경우
                check = 0 # 0점으로 
                break # for k 문 빠져나가기
        score[j] += check # 특정 플레이어의 점수 더하기

for sco in score:
    print(sco)
