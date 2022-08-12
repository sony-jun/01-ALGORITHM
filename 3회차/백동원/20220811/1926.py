# 그림
import sys
sys.stdin = open('1926.txt')

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
stack = []
cnt = 0
result = 0
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 1 and check[x][y] == False:
            cnt += 1
            size = 0
            stack.append((x, y))
            while len(stack) !=0:
                cur = stack.pop()
                if (matrix[cur[0]][cur[1]] == 1) and (check[cur[0]][cur[1]] == False):
                    check[cur[0]][cur[1]] = True
                    size += 1
                    for a in range(4):
                        mx = cur[0] + dx[a]
                        my = cur[1] + dy[a]
                        if 0 <= mx < n and 0 <= my < m and check[mx][my] == False and matrix[mx][my] == 1:
                            stack.append((mx, my))
            if size > result:
                result = size
print(cnt)
if cnt == 0:
    print(0)
else:
    print(result)