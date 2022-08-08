board = [list(map(int, input().split())) for _ in range(19)]

dx = [+1, +1, 0, -1]  # 행이동 하,우하,우,우상
dy = [0, +1, +1, +1]  # 열이동 하,우하,우,우상


def solution():
    for k in range(len(board)):
        for h in range(len(board[k])):

            if board[k][h] != 0:
                x, y = k, h  # 현재 좌표를 저장

                for i in range(4):  # 각 방향 이동
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board):
                        continue

                    startx, starty = x, y

                    count = 1

                    old_x, old_y = x, y  # 기존 x,y 값을 좌표계산을 위해 저장해놓는다.

                    # 좌표를 이동한 상태에서 만약 같은방향으로 같은 색 바둑이 있으면 그쪽으로 개수를 세면서 더 이동한다.
                    while True:
                        # 만약 다음 바둑이 현 바둑 색하고 똑같다면
                        if board[old_x][old_y] == board[nx][ny]:
                            count += 1  # 개수 1개 추가
                        else:  # 만약 색이 다르다면 반복문을 돌필요가 없기 때문에 반복문 탈출
                            break

                        # 만약 바둑 개수가 5개라면
                        if count == 5:
                            if len(board) > nx + dx[i] >= 0 and len(board) > ny + dy[i] >= 0:
                                if board[nx][ny] == board[nx + dx[i]][ny + dy[i]]:  # 6목이므로
                                    break

                            if 0 <= startx - dx[i] < len(board) and len(board) > starty - dy[i] >= 0:
                                if board[startx][starty] == board[startx - dx[i]][starty - dy[i]]:  # 6목이므로
                                    break

                            return [startx + 1, starty + 1, board[startx][starty]]

                        old_x, old_y = nx, ny  # 현재 좌표를 다음 이동 좌표로 저장
                        nx, ny = old_x + dx[i], old_y + dy[i]  # 다음 이동 좌표를 그 다음 다음 이동 좌표로 저장

                        # 만약 새로운 좌표가 범위를 벗어난다면 더이상 반복문을 돌 필요가 없으므로 탈출
                        if nx >= len(board) or ny >= len(board) or nx < 0 or ny < 0:
                            break


result = solution()

if result is None:
    print(0)
else:
    print(result[2])
    print(result[0], result[1])