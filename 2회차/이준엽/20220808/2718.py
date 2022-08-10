n,m = map(int,input().split())
matrix = [list(map(int,list((input())))) for i in range(n)]
visited = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def miro(x,y):
    if matrix[y][x] == 1:
        visited.append((x,y))
        for d in range(4):
            d_x = x+dx[d]
            d_y = y+dy[d]
            if matrix[d_y][d_x] == 1:
                miro(d_x,d_y)