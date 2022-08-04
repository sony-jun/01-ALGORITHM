import sys

input = sys.stdin.readline

n = int(input())
room = [list(input()) for _ in range(n)]

result = [0, 0]
#room 전체를 돌면서 
for i in range(n):
    row, column = 0, 0
    for j in range(n):
        # 가로 확인
        if room[i][j] != ".":
            row = 0
        else:
            row += 1
        if row == 2:
            result[0] += 1
        # 세로 확인
        if room[j][i] != ".":
            column = 0
        else:
            column += 1
        
        if column == 2:
            result[1] += 1

for i in result:
    print(i, end = " ")