from pprint import pprint
import sys

sys.stdin = open('1100.txt')

chess = [list(input()) for i in range(8)]

#pprint(chess)
cnt = 0

for row in range(8):
    for col in range(8):
        if chess[row][col] == 'F':
            if (row + col) % 2 == 0:
                cnt += 1
print(cnt)
