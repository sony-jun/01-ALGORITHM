import sys
input = sys.stdin.readline
# N X N 크기의 정사각형 방
# 빈 칸이 연속 2 칸 이상이면 누울 자리
# 가로로, 세로로 누울 수 있음
# 누울 때는 반드시 벽이나 짐에 닿게 된다!
N = int(input())
room = [list(input().rstrip()) for _ in range(N)]
가로자리합 = 0
세로자리합 = 0
for i in range(N):
    cnt = 0

    for j in range(N):
        if room[i][j] == '.':
            cnt += 1 # cnt는 '.'을 만나면 더한다.
        else: # 'X'를 만나는 경우
            if cnt >= 2: # cnt가 2개 이상이면
                가로자리합 += 1 # 누울 자리가 있기 때문에 가로자리합에 1을 더한다.
                cnt = 0 # cnt의 개수 다시 초기화
            else:
                cnt = 0
    if cnt >= 2: # 'X'를 만나지 않았지만 cnt('.')이 2개 이상이면
        가로자리합 += 1 # 가로자리합에 1을 더한다.

# transpose (열 순회)
room2 = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        room2[i][j] = room[j][i]

for i in range(N):
    cnt = 0
    
    for j in range(N):
        if room2[i][j] == '.':
            cnt += 1 # cnt는 '.'을 만나면 더한다.
        else: # 'X'를 만나는 경우
            if cnt >= 2: # cnt가 2개 이상이면
                세로자리합 += 1 # 누울 자리가 있기 때문에 세로자리합에 1을 더한다.
                cnt = 0 # cnt의 개수 다시 초기화
            else:
                cnt = 0
    if cnt >= 2: # 'X'를 만나지 않았지만 cnt('.')이 2개 이상이면
        세로자리합 += 1 # 세로자리합에 1을 더한다.

print(가로자리합, 세로자리합)