import sys
sys.stdin = open('./2178.txt')


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

x, y = 0, 0
dx = [1, 0]
dy = [0, 1]
dx2 = [0, -1]
dy2 = [-1, 0]
while True:
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        nx2 = x + dx2[d]
        ny2 = x + dy2[d]
        if matrix[ny][nx] == '1' and 0 <= ny <= n - 1 and 0 <= nx <= m - 1:
            
            x += dx[d]
            y += dy[d]
            print('들어옴', x, y)
        elif matrix[ny2][nx2] == '1' and 0 <= ny2 <= n - 1 and 0 <= nx2 <= m - 1:
            
            x += dx2[d]
            y += dy2[d]
            print('자리가 없네', x, y)


        if x == 4:
            break
