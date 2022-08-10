import sys
sys. stdin = open("38_오목.txt")

N = 19

B = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 1, 1]
dy = [0, 0, -1, 1]


for x in range(N):
    for y in range(N):
        if B[x][y] != 0: # 바둑판에 돌이 있을 때 
            for i in range(4): # 인덱스로 같은 돌이 있는 방향 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1

                while not 0 <= nx < N and 0 <= ny < N and B[x][y] == B[nx][ny]:
                        cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                        
                        # 육목찾기
                        if cnt == 5:
                            if 0 <= x-dx[i] < N and 0 <= y-dy[i] < N and B[x][y] == B[x-dx[i]][y-dy[i]]:
                                break
                            if 0 <= nx < N and 0 <= ny < N and B[x][y] == B[nx][ny]:
                                break
                            print(B[x][y])
                            print(x + 1, y + 1)
                            break
print(0)