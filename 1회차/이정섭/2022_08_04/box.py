for i in range(int(input())):
    m, n = map(int, input().split())
    grid = [[] for i in range(n)]

    for j in range(m):
        a = list(input().split())
        for k in range(n):
            grid[k].append(a[k])

    move_cnt = 0
    for j in range(m):
        box = grid[j].count('1')
        floor = m - 1

        for k in range(m-1, -1 -1):
            if grid[j][k] == '1':
                move_cnt += floor - j
                floor -= 1
            
    print(move_cnt)