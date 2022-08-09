# https://www.acmicpc.net/problem/2178

N, M = map(int,input().split())

matrix = [input() for _ in range(N)]

# 오른쪽 > 아래 > 위 > 왼쪽
dx = [0, 1, -1, 0] 
dy = [1, 0, 0, -1]
count = 1
row = 0
col = 0


while True:
    for i in range(4):
        x = row+dx[i]
        y = col+dy[i] 

        if 0 <= x < N and 0 <= y < M:
            if matrix[x][y] == '1':
                row = x
                col = y
                count+=1
                break
            elif  matrix[x][y] == '0':
                continue
        elif row == N-1 and col == M-1:
            print(count)
            exit(0)
    # if row == N-1 and col == M-1:
    #     break
