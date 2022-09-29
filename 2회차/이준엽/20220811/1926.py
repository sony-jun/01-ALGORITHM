n,m = map(int,input().split())
paper = [list(map(int,input().split())) for i in range(n)]
visited = [list(False for i in range(m)) for i in range(n)]
cnt = 0
delta = [(-1,0),(1,0),(0,-1),(0,1)]
sq_list = []
stack = []

for sy in range(n):
    for sx in range(m):
        if paper[sy][sx] == 1 and visited[sy][sx] == False:
            sq = 1
            visited[sy][sx] = True
            stack.append((sy,sx))
            while stack:
                start = stack.pop()
                y = start[0]
                x = start[1]
                for d in range(4):
                    d_x = x+delta[d][1]
                    d_y = y+delta[d][0]
                    if 0<=d_x<m and 0<=d_y<n:
                        if paper[d_y][d_x] == 1 and visited[d_y][d_x] == False:
                            visited[d_y][d_x] = True
                            stack.append((d_y,d_x))
                            sq +=1
            sq_list.append(sq)
            cnt+=1

print(cnt)
if sq_list == []:
    print(0)
else:
    print(max(sq_list))