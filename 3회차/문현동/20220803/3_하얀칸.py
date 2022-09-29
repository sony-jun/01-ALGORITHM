import sys
from pprint import pprint
sys.stdin = open("3_하얀칸.txt", 'r')

chess_board = []
cnt = 0

for cell in range(8):
    chess_board.append(list(sys.stdin.readline().rstrip()))
    
for w in range(8):
    for h in range(8):
        if (w + h) % 2 == 0:
            if chess_board[w][h] == 'F':
                cnt += 1

print(cnt)