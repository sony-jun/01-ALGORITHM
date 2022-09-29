dy = [0, 1, -1]
dx = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

board = []

for _ in range(N):

    temp_list = list(map(int, input().split()))
    board.append(temp_list)

for y in range(N):
    for x in range(N):

        for d in range(4):
            stone_count = 0
            ny = y + dy[d]
            nx = x + dx[d]

            while True:

                if not(-1 < ny < N and -1 < nx < N):
                    break
                if not(board[y][x] == board[ny][nx]):
                    break

                stone_count += 1

            ny = ny + dy[d]
            nx = nx + dx[d]
        
        if stone_count == 5:
            prev_y = y - dy[d]
            prev_x = x - dx[d]

            if not(-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                print(board[y][x])
                print(y + 1, x + 1)




edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [2, 5],
    [4, 6]
]
# 정점 개수 == 7개 

n = 7

# n X n 행렬 0으로 초기화
metrix = [[0] * n for _ in range(n)]

for edge in edges:
    v1, v2 = edge[0], edge[1]
    metrix[v1][v2] = 1
    metrix[v2][v1] = 1
