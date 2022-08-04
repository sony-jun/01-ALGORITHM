import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    grid = [[] for _ in range(n)]
    for i in range(m):
        mat = list(input().split())
        for g in range(n):
            grid[g].append(mat[g])
    
    cnt = 0
    
    for i in range(n):
        n = mat[i].count('1')
        f = m - 1
        
        for j in range(m-1, -1, -1):
            if grid[i][j] == '1':
                cnt += f-j
                f -= 1
    
    print(cnt)