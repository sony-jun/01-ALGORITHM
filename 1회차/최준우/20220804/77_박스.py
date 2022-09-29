# https://www.acmicpc.net/problem/9455

T = int(input())

for test_case in range(T):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0

    for j in range(n):
        for i in range(m):
            if grid[i][j] == 1:
                for k in range(i+1, m):
                    if grid[k][j] == 0:
                        cnt += 1
    print(cnt)