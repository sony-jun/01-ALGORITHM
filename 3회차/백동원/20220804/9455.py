# 박스

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    cnt_ = 0
    for a in range(n):
        for b in range(m):
            cnt = 0
            if grid[b][a] == 1:
                for c in range(b + 1, m):
                    if grid[c][a] == 0:
                        cnt += 1
                cnt_ += cnt
    print(cnt_)