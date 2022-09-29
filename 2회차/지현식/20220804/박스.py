for test_case in range(int(input())):
    m, n = map(int, input().split())
    grid = [list(input().split()) for _ in range(m)]
    grid = list(map(list, zip(*grid)))
    cnt = 0

    for i in range(n):
        ground = m - 1
        for j in range(m - 1, -1, -1):
            if grid[i][j] == "1":
                cnt += ground - j
                ground -= 1
    print(cnt)