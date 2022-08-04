n = int(input()) # 지뢰가 있는 행의 갯수

m = [list(input()) for _ in range(n)] 
a = [list(input()) for _ in range(n)] 
result = [['.'] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    for j in range(n):
        # 칸을 열었는데 지뢰가 아닌 경우
        if m[i][j] == '.' and a[i][j] == 'x':
            cnt = 0
            # a[i][j]를 중심으로 8방향의 지뢰 학인
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                # 인덱스를 넘어가는 경우 예외처리
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if m[nx][ny] == '*':
                    cnt += 1
            result[i][j] = cnt
        # 칸을 열었는데 지뢰인 경우 > 게임종료 > 모든 지뢰를 표시
        if m[i][j] == '*' and a[i][j] == 'x':
            for p in range(n):
                for q in range(n):
                    if m[p][q] == '*':
                        result[p][q] = '*'

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print()