import sys
input = sys.stdin.readline

N = int(input())
row = 0
column = 0

room = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    temp = 0
    for j in range(1, N):
        if room[i][j-1] == '.' and room[i][j] == '.':
            temp += 1
        elif room[i][j] == 'X':
            if temp:
                row += 1
            temp = 0
    if temp:
        row += 1

room = list(map(list, zip(*room)))
for i in range(N):
    temp = 0
    for j in range(1, N):
        if room[i][j-1] == '.' and room[i][j] == '.':
            temp += 1
        elif room[i][j] == 'X':
            if temp:
                column += 1
            temp = 0
    if temp:
        column += 1

print(row, column)