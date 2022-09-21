import sys
sys.stdin = open("121_섬의 개수_4963.txt", "r")
from collections import deque


# DFS
def dfs(x, y):

    # 델타 이동
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [1, -1, 1, -1, 0, 0, 1, -1]

    q = deque()
    q.append([x, y])

    while q:
        a, b = q.popleft()

        # 8방향 델타 탐색
        for i in range(8):
            
            # 델타 이동
            nx = a + dx[i]
            ny = b + dy[i]

            # 범위 벗어나지 않고 && 섬 발견하면 dfs
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                # 방문 처리 (0으로 만들어야 델타 이동시 중복 계산X)
                graph[nx][ny] = 0
                q.append([nx, ny])



while True:
    # w, h 입력
    w, h = map(int, input().split())
    
    # 0, 0 만나면 종료
    if w == 0 and h == 0:
        break
    
    # h번 만큼 반복하며 리스트 생성
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    # 카운트 변수
    cnt = 0

    # 그래프 탐색하며, 섬 발견하면 DFS, 이후 탐색 끝나면 cnt += 1
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)