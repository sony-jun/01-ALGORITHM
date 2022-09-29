import sys
sys.stdin = open("input.txt")
read = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def dfs(x, y):
    # 현재 값을 0으로 바꾸기
    earth[x][y] = 0

    # 8방위 탐색
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 판을 나가지 않고 탐색한 다음 값이 1이면
        if -1 < nx < h and -1 < ny < w and earth[nx][ny] == 1:
            # 탐색한 다음 값 2로 바꾸기
            earth[nx][ny] = 2
            # 탐색한 다음 값으로 dfs 탐색 재귀
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())

    # 입력으로 0 0이 주어지만 반복문 빠져나가기
    if w == 0 and h == 0:
        break

    # 2차원 리스트 입력받기
    earth = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    # earth 순회
    for i in range(h):
        for j in range(w):
            # earth 값이 1이면
            if earth[i][j] == 1:
                # i, j에 대해 dfs 탐색
                dfs(i, j)
                # 탐색이 끝난 후 cnt에 1 더하기
                cnt += 1
    print(cnt)