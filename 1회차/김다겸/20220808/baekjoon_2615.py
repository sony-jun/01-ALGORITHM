import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# 아래, 오른쪽 아래, 오른쪽 , 오른쪽 위
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]


# 오목판 순회
for x in range(19):
    for y in range(19):
        # 오목이 1이나 2이면(0이 아니면)
        if board[x][y]:
            # nx, ny 방향 설정
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 연속된 오목 개수 위한 cnt 변수 1로 초기화
                cnt = 1
                
                # 오목판 안에 있고, 현재 값이랑 다른 방향으로 움직인 값이 같으면
                while 0 <= nx < 19 and 0 <= ny < 19 and board[x][y] == board[nx][ny]:
                    # cnt에 1 더하기
                    cnt += 1
                    # cnt가 5이면
                    if cnt == 5:
                        # 다음 알이 판 안에 있고, 현재 알과 다음 알이 같으면(육목이면)
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[x][y] == board[nx + dx[i]][ny + dy[i]]:
                            # 멈추기
                            break
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x][y] == board[x - dx[i]][y - dy[i]]:
                            break
                        # 오목이면 알의 값과 위치 출력하고 종료
                        print(board[x][y])
                        print(x + 1, y + 1)
                        sys.exit(0)
                    # while문 안에서 오목 위치 하나씩 더해주기
                    nx += dx[i]
                    ny += dy[i]

print(0)