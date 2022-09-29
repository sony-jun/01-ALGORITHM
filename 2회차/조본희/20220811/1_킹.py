import sys
from pprint import pprint
# sys.stdin = open('input.txt')
input = sys.stdin.readline

king, stone, n = map(list, input().split())
n = int(''.join(n))

board = [[0] * 8 for _ in range(8)]
king[0] = ord(king[0]) - 65
king[1] = abs(int(king[1]) - 8)
king.reverse()
stone[0] = ord(stone[0]) - 65
stone[1] = abs(int(stone[1]) - 8)
stone.reverse()
board[king[0]][king[1]] = 1
board[stone[0]][stone[1]] = 2

movetrans = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],
    'RB': [1, 1],
    'LB': [1, -1]
}

for _ in range(n):
    move = input().rstrip()
    dx = movetrans[move][0]
    dy = movetrans[move][1]
    knx = king[0] + dx
    kny = king[1] + dy
    snx = stone[0] + dx
    sny = stone[1] + dy
    # print(snx, sny)

    if 0 <= snx < 8 and 0 <= sny < 8 and 0 <= knx < 8 and 0 <= kny < 8:
        if board[knx][kny] == 2:
            board[snx][sny] = 2
            stone[0] = snx
            stone[1] = sny
        board[knx][kny] = 1
        board[king[0]][king[1]] = 0
        king[0] = knx
        king[1] = kny

    #킹은 움직이고 돌은 안움직이는경우
    elif 0 <= knx < 8 and 0 <= kny < 8 and board[knx][kny] != 2:
        board[knx][kny] = 1
        board[king[0]][king[1]] = 0
        king[0] = knx
        king[1] = kny

    # pprint(board)

king.reverse()
stone.reverse()
print(chr(king[0] + 65), abs(king[1] - 8), sep='')
print(chr(stone[0] + 65), abs(stone[1] - 8), sep='')