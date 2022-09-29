import sys
from pprint import pprint
sys.stdin = open('하얀칸_input.txt')

n = 8
m = 8
cnt = 0

chess = [list(input()) for i in range(8)]
# [['.', 'F', '.', 'F', '.', '.', '.', 'F'],
#  ['F', '.', '.', '.', 'F', '.', 'F', '.'],
#  ['.', '.', '.', 'F', '.', 'F', '.', 'F'],
#  ['F', '.', 'F', '.', '.', '.', 'F', '.'],
#  ['.', 'F', '.', '.', '.', 'F', '.', '.'],
#  ['F', '.', '.', '.', 'F', '.', 'F', '.'],
#  ['.', 'F', '.', 'F', '.', 'F', '.', 'F'],
#  ['.', '.', 'F', 'F', '.', '.', 'F', '.']]
# 좌표를 더해서 짝수는 하얀칸 홀수는 검은 칸
for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0 and chess[i][j] == 'F':
            cnt += 1
# pprint(chess)
print(cnt)