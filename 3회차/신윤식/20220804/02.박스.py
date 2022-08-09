T = int(input())

for _ in range(T):
    m, n = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(m)]
    count = 0

    for col in range(n):
        reset = 1
        while True:
            if reset == 0:
                break
            reset = 0
            for row in range(m-1,0,-1):
                if grid[row][col] == 0:
                    if grid[row-1][col] == 1:
                        grid[row-1][col], grid[row][col] = grid[row][col], grid[row-1][col]
                        count += 1
                        reset += 1
    print(count)