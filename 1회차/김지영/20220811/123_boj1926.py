import sys
sys.stdin = open('1926.txt')

dy = [0, 0 ,1, -1]
dx = [1, -1, 0, 0]
   
# 입력 받기
n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
cnt = 0
painting_size_list = []
for sy in range(n):
    for sx in range(m):
        if not visited[sy][sx] and graph[sy][sx] == 1:
            stack = []
            stack.append((sy,sx))
            visited[sy][sx] = True
            
            cnt += 1
            # 그림의 넓이? = pop횟수
            painting_size = 0
            while len(stack) != 0:
                y,x = stack.pop()
                painting_size += 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (-1 < ny < n and -1 < nx < m):
                        continue
                    if visited[ny][nx] == True:
                        continue
                    if graph[ny][nx] != 1:
                        continue
                    if -1 < ny < n and -1 < nx < m :
                        stack.append((ny,nx))
                        y = ny
                        x = nx
                painting_size_list.append(painting_size)
if len(painting_size_list) != 0:
    print(painting_size_list)
    print(cnt)
else : print('0\n0')