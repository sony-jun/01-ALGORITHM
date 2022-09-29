import sys
sys.stdin = open("20220803/1236_성지키기.txt")

N, M = map(int,input().split())                     # 행, 열

castle = []                                         # 성의 현재 상황
for i in range(N):
    castle.append(list(input()))                    # 2차원 배열

N_guard = 0                                         # 행 추가 경비 수
M_guard = 0                                         # 열 추가 경비 수

for n in range(N):
    if "X" not in castle[n]:                        # 경비가 없는 행
        N_guard += 1                                # 없으면 경비 추가

for m in range(M):
    if "X" not in [castle[n][m] for n in range(N)]: # 경비가 없는 열
        M_guard += 1                                # 없으면 경비 추가

print(max(N_guard ,M_guard))                        # 둘 중에 큰 값 출력