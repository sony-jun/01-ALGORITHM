# n = 19
# dy = [0,1,-1,1]
# dx = [1,0,1,1]

# board = [list(map(int,input().split())) for i in range(n)]
# answer = 0
# for y in range(n):
#     for x in range(n):
#         if board[y][x] == 1 or board[y][x] == 2:
#             for d in range(4):
#                 stone_count = 1
#                 ny = y+dy[d]
#                 nx = x+dx[d]

#                 while True:
#                     if not (0<=ny<n and 0<=nx<n ):
#                         break
#                     if not (board[y][x] == board[ny][nx]):
#                         break

#                     stone_count +=1
#                     ny = ny+dy[d]
#                     nx = nx+dx[d]
                
#                 if stone_count == 5:
#                     prevy = y - dy[d]
#                     prevx = x - dx[d]
#                     if not (0<=prevx<n and 0<=prevy<n) or board[y][x] != board[prevy][prevx]:
#                         answer = board[y][x]
#                         coord = [y+1,x+1]

# if answer == 0:
#     print(answer)
# else:
#     print(answer)
#     print(*coord)


graph = []
for _ in range(19):
    graph.append(list(map(int,input().split())))
answer =0
delta = [(-1,1),(0,1),(1,0),(1,1)]

for y in range(19):
    for x in range(19):
        if graph[y][x] == 1 or graph[y][x] == 2:
            cnt = 1
            for d in delta:
                dy = y + d[0]
                dx = x + d[1]
                
                while True:
                    if not (0<=dy<19 and 0<=dx<19):
                        break
                    if graph[y][x] != graph[dy][dx]:
                        break
                    else:
                        dy = dy + d[0]
                        dx = dx + d[1]
                        cnt +=1
                if cnt == 5:
                    
                    prex = x - d[1]
                    prey = y - d[0]
                    if not (0<=prex<19 and 0<=prey<10) or graph[prey][prex] != graph[y][x]:
                        answer = graph[y][x]
                        coord = [y+1,x+1]
                       
if answer == 0:
    print(0)
else:
    print(answer)
    print(*coord)