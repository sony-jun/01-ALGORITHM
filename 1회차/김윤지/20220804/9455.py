
t = int(input())

for _ in range(t):
    m, n = map(int,input().split())
    tetris = [list(map(str,input().split()))for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if tetris[i][j] == '1':
                cnt += 1


#모르ㅔㄱ써요ㅠㅠ