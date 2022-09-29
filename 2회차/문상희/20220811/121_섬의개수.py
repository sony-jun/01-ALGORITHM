import sys
sys.stdin = open('test.txt', 'r')

while True:
    x, y = list(map(int, input().split()))
    if y == 0 and x == 0:
        break
    pic = []
    for _ in range(y):
        line = list(map(int, input().split()))
        pic.append(line)

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    def dfs(a, b):
        for c in range(8):
            ni = a + di[c]
            nj = b + dj[c]
            if ni in range(y):
                if nj in range(x):
                    if pic[ni][nj] == 1:
                        pic[ni][nj] = 0
                        dfs(ni, nj)
    
    cnt = 0
    for i in range(y):
        for j in range(x):
            if pic[i][j] == 1:
                cnt += 1
                dfs(i, j)
    
    print(cnt)