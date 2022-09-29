# 19개 줄로 짜고, 8방향 DFS, 출력할 때 x += 1, y += 1
import sys
sys.stdin = open("94_오목_2615.txt", "r")

# 입력 받아서, 그래프 생성
graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))

# 델타: 우, 하, 우하, 좌하
dx = [0, 1, 1]
dy = [1, 0, 1]

def omok():
    for x in range(19):
        for y in range(19):
            if graph[x][y]:
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                        continue

                    while 0 <= nx < 19 and 0 <= ny < 19 and graph[x][y] == graph[nx][ny]:
                        cnt += 1

                        # 카운트가 5에 도달하면
                        if cnt == 5:
                            # 다음 돌 탐색
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and graph[nx][ny] == graph[nx + dx[i]][ny + dy[i]]:
                                break
                            # 처음 -1번째 돌 탐색
                            if 0 <= nx - dx[i] < 19 and 0 <= ny - dy[i] < 19 and graph[x][y] == graph[x - dx[i]][y - dy[i]]:
                                break
                            return graph[x][y], x+1, y+1
                        
                        nx += dx[i]
                        ny += dy[i]
        
    return 0, -1, -1                    

color, x, y = omok()

if not color:
    print(color)
else:
    print(color)
    print(x, y)