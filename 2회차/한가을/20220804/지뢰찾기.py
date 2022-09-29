# 4396
# 첫 번째 줄에는 10보다 작거나 같은 양의 정수 n이 입력
# 다음 n개의 줄은 지뢰의 위치를 나타낸다
# 각각의 줄은 n개의 문자를 사용하여 한 행을 나타낸다
# '.'은 지뢰가 없는 지점이며 '*'는 지뢰가 있는 지점
# 다음 n개의 줄에는 길이가 n인 문자열이 입력
# 이미 열린 칸은 영소문자 x로, 열리지 않은 칸은 '.' 으로 표시

# 각각의 위치가 정확하게 채워진 판을 표현해 출력
# 지뢰가 없으면서 열린 칸에는 0과 8 사이의 숫자가 있어야 함
# 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 '*'로 표시
# 다른 모든 지점은 '.'

import sys
sys.stdin = open('지뢰찾기.txt')

n = int(input())
mine = [list(input()) for _ in range(n)]
board = [list(input()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(n):
    for y in range(n):
        #* 지뢰가 없으면서 열린 칸
        if mine[x][y] == '.' and board[x][y] == 'x':
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >=n:
                    continue

                if mine[nx][ny] == '*':
                    cnt += 1
            #* 33번의 조건절을 통과하지 않아도 cnt 적용
            result[x][y] = cnt
        
        #* 지뢰가 있는 칸이 열렸다면
        if mine[x][y] == '*' and board[x][y] == 'x':
            for a in range(n):
                for b in range(n):
                    #* 첫번째 입력 중 지뢰가 있는 칸이면
                    if mine[a][b] == '*':
                        #* 지뢰가 있는 모든 칸을 별표로 표시
                        result[a][b] = '*'

for i in range(n):
    for j in range(n):
        print(result[i][j], end = '')
    print()