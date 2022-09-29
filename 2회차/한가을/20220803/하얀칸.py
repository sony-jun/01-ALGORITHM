# 백준 1100
# 체스판은 8x8 크기이고 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다
# 가장 왼쪽 위칸 (0, 0)은 하얀색
# 체스판의 상태가 주어졌을 때
# 하얀 칸 위에 말이 몇개 있는지 출력
# '.'은 빈 칸이고 'F'는 위에 말이 있는 칸

import sys
sys.stdin = open('하얀칸.txt', 'r')

board = []

# 체스판 입력
for _ in range(8):
    board.append(list(map(str, input())))

# 흰샌칸 위의 말 개수를 담을 변수 선언
result = 0

# 체스판 전체 탐색
for i in range(8):
    for j in range(8):
        # 체스판의 위치가 2로 나누어 떨어지면서
        # 그 위에 말이 있다면
        if (i + j) % 2 == 0 and board[i][j] == 'F':
            # 말 개수 증가
            result += 1

print(result)