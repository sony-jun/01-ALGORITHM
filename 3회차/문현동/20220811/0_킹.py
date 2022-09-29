import sys
from pprint import pprint
sys.stdin = open("0_킹.txt", 'r')

king_position_set, stone_position_set, N = sys.stdin.readline().split()
N = int(N)

board = []
move_to = []

for _ in range(8):
    board.append([' '] * 8) # 보드 만들기

for _ in range(N):
    move_to.append(sys.stdin.readline().rstrip()) # 이동 명령어 리스트

delta =\
    {
    'T' : (-1, 0),
    'RT' : (-1, 1),
    'R' : (0, 1),
    'RB' : (1, 1),
    'B' : (1, 0),
    'LB' : (1, -1),
    'L' : (0, -1),
    'LT' : (-1, -1),
    } # 알파벳에 대응하는 이동방향 딕셔너리

board[8 - int(king_position_set[1])][ord(king_position_set[0]) - 65] = 'K'
board[8 - int(stone_position_set[1])][ord(stone_position_set[0]) - 65] = 'S' # 수업시간에 배운대로 만듦
# [T, RB, R ... ]
i = 0
for num in range(7, -1, -1): # 아래 행부터 탐색해야 빠르다.
    for alpha in range(8):
        if board[num][alpha] == 'K':
            while i < N: # 주어진 이동 명령어만큼 반복
                n_num = num + delta[move_to[i]][0] # 일단 값을 갱신하고
                n_alpha = alpha + delta[move_to[i]][1]
                if -1 < n_num < 8 and -1 < n_alpha < 8: # 그 값이 범위에 벗어나지 않는다면
                    if board[n_num][n_alpha] == 'S': # 또한 만약 이동된 좌표에 돌이 있다면
                        if -1 < n_num + delta[move_to[i]][0] < 8 and -1 < n_alpha + delta[move_to[i]][1] < 8: # 또한 만약 돌의 다음 이동예정지가 범위를 벗어나지 않는다면
                            board[num][alpha] = ' ' # 현 위치는 비우고
                            board[n_num][n_alpha] = 'K' # 이동 좌표에 킹을 놓고
                            board[n_num + delta[move_to[i]][0]][n_alpha + delta[move_to[i]][1]] = 'S' # 이동 좌표의 다음 방향으로 돌을 놓음
                            num = n_num # 다음 탐색을 위한 좌표 갱신
                            alpha = n_alpha
                    else:
                        board[n_num][n_alpha] = 'K'
                        board[num][alpha] = ' '
                        num = n_num
                        alpha = n_alpha
                i += 1

for num in range(7, -1, -1):
    for alpha in range(8):
        if board[num][alpha] == 'K':
            king_position = str(chr(65 + alpha)) + str(8 - num)
        if board[num][alpha] == 'S':
            stone_position = str(chr(65 + (alpha))) + str(8 - num)

print(king_position)
print(stone_position)