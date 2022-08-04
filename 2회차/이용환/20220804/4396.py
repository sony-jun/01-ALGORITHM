import sys
input = sys.stdin.readline
T = int(input())
matrix1 = [list(input().rstrip()) for _ in range(T)] # 폭탄 지도
matrix2 = [list(input().rstrip()) for _ in range(T)] # 사용자가 열은 지도
result = [['.'] * T for _ in range(T)] # 출력해야 할 결과 값
ax = [-1, -1, 0, 1, 1, 1, 0, -1] # x 가 가능한 방향값
ay = [0, 1, 1, 1, 0, -1, -1, -1] # y 가 가능한 방향값
for x in range(T):
    for y in range(T):
        if matrix1[x][y] == '.' and matrix2[x][y] == 'x': # 사용자가 열었는데 폭탄이 없을 경우
            cnt = 0 # 폭탄 초기값
            for i in range(8): # 8방향 탐색
                bx = x + ax[i]
                by = y + ay[i]
                if bx < 0 or by < 0 or bx >= T or by >= T: # 8x8 일 경우 인덱스는 0~7까지 존재하기 때문에 벗어 났을 경우 계속 탐색
                    continue
                if matrix1[bx][by] == '*': #8 방향중에 폭탄이 있으면
                    cnt += 1 # cnt + 1
            result[x][y] = cnt # 8 방향 폭탄 갯수 만큼 결과 값에 '.' 대신 숫자 입력
        if matrix1[x][y] == '*' and matrix2[x][y] == 'x': # 사용자가 열었는데 폭탄이 있을 경우
            for j in range(T):
                for k in range(T): # 모든 자리에 폭탄을 넣어야 함.
                    if matrix1[j][k] == '*': # 폭탄이 있는 자리에
                        result[j][k] = '*' # 결과 값에 기존에 있던 '.' 을 폭탄으로 변경
for i in result:
    for j in i:
        print(j, end='')
    print()