import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    # x, y가 판 안에 있다면
    if 0 <= x < h and 0 <= y < w:
        # 값이 1이라면
        if earth[x][y] == 1:
            # 2로 바꾼 후
            earth[x][y] = 2
            # 8방위 탐색
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    cnt = 0
    earth = []

    for i in range(h):
        earth.append(list(map(int, read().split())))
    for i in range(h):
        for j in range(w):
            # 값이 1이라면
            if earth[i][j] == 1:
                # i, j에 대해 dfs 탐색
                dfs(i, j)
                # 횟수 더하기
                cnt += 1
    print(cnt)