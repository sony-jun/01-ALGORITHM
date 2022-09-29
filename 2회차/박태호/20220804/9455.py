# 박스
# 행 = m , 열 = n
# 5 4
import sys
sys.stdin = open('박스.txt','r')

for _ in range(int(input())):
    m,n = map(int, input().split())
    grid = [[] for _ in range(n)]
    for i in range(m):
        a = list(input().split()) #  행우선으로 정렬
        for j in range(n):
            grid[j].append(a[j])
    print(grid) # 열 우선 정렬
    movecnt = 0
    for i in range(n): # 4
        boxnum = (grid[i].count('1'))
        floor = m - 1
        for j in range(m-1,-1,-1):
            if grid[i][j] == '1':
                movecnt += floor - j
                floor -= 1
    print(movecnt)