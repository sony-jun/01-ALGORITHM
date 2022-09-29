board = [[3]+list(map(int, input().split()))+[3] for _ in range(19)]
line = [3]*21
board.insert(0, line)
board.append(line)
# 오목판을 행렬로 받으며, 인덱스 초과를 해결하기 위해 주변에 테두리를 둘러줌.
def omok(board, x, y) :
    ans = 0
    dx = [-1, 0, 1, 1] # 오목 성공시 가장 왼쪽알중 가장 위쪽 알을 출력해야하므로 이렇게 4방향을 설정했다.
    dy = [1, 1, 0, 1]
    if board[x][y] != 0 :
        a = board[x][y] # 해당 돌이 흑인지 백인지 판별하는 변수 
        for i in range(4) :
            x_ = x
            y_ = y
            go = 1 # 연속된 바둑알의 개수를 세어준다

            if (board[x_-dx[i]][y_-dy[i]] != a) : # 해당 방향의 바로 전 칸이 a일 경우 이미 확인했던 칸이므로 아닐 경우에만 확인한다.
                for _ in range(6) :
                    x_ += dx[i]
                    y_ += dy[i]
                    if board[x_][y_] == a :
                        go += 1 # 한 방향으로 같은 바둑알이 연속으로 있을 경우 +1
                        if go == 5 :
                            ans = a
                        if go == 6 :
                            ans = 0
                    else :
                        break
    return ans

for x in range(1, 20) :
    for y in range(1, 20) :
        win= omok(board, x, y)
        if win != 0 :
            print(win)
            print(x, y)
            exit(0)
print(0) # 모든 판을 검사 한 후에도 승리 조건을 채우지 못할 