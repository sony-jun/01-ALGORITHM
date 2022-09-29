# 4963
# n, m = map(int, input().split())

# # 상하좌우 + 대각선
# dx = [-1, 1, 0, 0, -1, 1, -1, 1]
# dy = [0, 0, -1, 1, -1, -1, 1, 1]


# # 2.이차원 리스트 순회
# for x in range(n):
#     for y in range(m):

#         # 3.델타값을 이용해 상하좌우 이동
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 4.범위를 벗어나지 않으면 갱신
#             if 0 <= nx < n and 0 <= ny < m:
#                 x = nx
#                 y = ny

# 시계 방향
dX = [1, 1, 0, -1, -1, -1, 0, 1]
dY = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    def DFS(x, y, mapList, visitedList):
        visitedList[y][x] = True  # 방문 완료

        for i in range(8):
            nX = x + dX[i]
            nY = y + dY[i]

            if 0 <= nX < w and 0 <= nY < h:
                if visitedList[nY][nX] == False and mapList[nY][nX] == 1:
                    DFS(nX, nY, mapList, visitedList)

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapList = []
    for i in range(h):
        mapList.append(list(map(int, input().split())))
    visitedList = [list(False for _ in range(w)) for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if visitedList[i][j] == False and mapList[i][j] == 1:
                DFS(j, i, mapList, visitedList)
                count += 1

    print(count)