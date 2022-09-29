import sys
from pprint import pprint
sys.stdin = open("3_지뢰찾기.txt", 'r')

N = int(sys.stdin.readline())

mine = []
progress = []
plane = []
mine_check = False

for _ in range(N + 2):
    plane.append([0] * (N + 2))

for _ in range(N):
    mine.append(sys.stdin.readline().rstrip())

for _ in range(N):
    progress.append(list(sys.stdin.readline().rstrip()))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if mine[i - 1][j - 1] == '*':
            
            plane[i - 1][j - 1] += 1
            plane[i - 1][j] += 1
            plane[i - 1][j + 1] += 1
            
            plane[i][j - 1] += 1
            plane[i][j + 1] += 1
            
            plane[i + 1][j - 1] += 1
            plane[i + 1][j] += 1
            plane[i + 1][j + 1] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if mine[i - 1][j - 1] == '*':
            plane[i][j] = '*'

for r in range(len(plane)):
    for c in range(len(plane)):
        plane[r][c] = str(plane[r][c])

for i in range(N):
    for j in range(N):
        if progress[i][j] == 'x':
            progress[i][j] = plane[i + 1][j + 1]
            if progress[i][j] == '*':
                mine_check = True


for i in range(N):
    for j in range(N):
        if mine_check:
            if progress[i][j] == '.':
                progress[i][j] = mine[i][j]
    progress[i] = ''.join(progress[i])
    print(progress[i])