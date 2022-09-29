import sys
sys.stdin = open("20220804/1652_누울자리를찾아라.txt")

N = int(input())

condo = []                                      # 콘도 방 상황
for n in range(N):
    condo.append(list(input()))                 # 2차원 배열

garo, sero = 0, 0                               # 가로, 세로 누울 수 있는 자리 수

for i in range(N):                              # 가로 확인
    cnt = 0                                     # 빈 공간 크기
    for j in range(N):
        if condo[i][j] == '.' and j < N-1:      # 방 끝이 아닌데 빈 공간이 있으면
            cnt += 1                            # 빈 공간 크기 +1

        elif condo[i][j] == '.' and j == N-1:   # 방 끝인데 빈 공간이 있으면
            cnt += 1                            # 빈 공간 크기 +1
            if cnt >= 2:                        # 빈 공간이 2자리 이상일 때
                garo += 1                       # 누울 수 있으므로 자리 수 +1
        
        elif condo[i][j] == 'X':                # 짐이 있는 공간이면
            if cnt >= 2:                        # 빈 공간이 2자리 이상일 때
                garo += 1                       # 누울 수 있으므로 자리 수 +1
            cnt = 0                             # 빈 공간 크기 초기화

for j in range(N):                              # 세로 확인
    cnt = 0                                     # 빈 공간 크기
    for i in range(N):
        if condo[i][j] == '.' and i < N-1:      # 방 끝이 아닌데 빈 공간이 있으면
            cnt += 1                            # 빈 공간 크기 +1

        elif condo[i][j] == '.' and i == N-1:   # 방 끝인데 빈 공간이 있으면
            cnt += 1                            # 빈 공간 크기 +1
            if cnt >= 2:                        # 빈 공간이 2자리 이상일 때
                sero += 1                       # 누울 수 있으므로 자리 수 +1

        elif condo[i][j] == 'X':                # 짐이 있는 공간이면
            if cnt >= 2:                        # 빈 공간이 2자리 이상일 때
                sero += 1                       # 누울 수 있으므로 자리 수 +1
            cnt = 0                             # 빈 공간 크기 초기화

print(garo, sero)                               # 가로, 세로 누울 수 있는 자리 수 출력