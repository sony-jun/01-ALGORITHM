from re import A
import sys
sys.stdin = open("성지키기.txt")

n, m = map(int, input().split())
security_list = []

for _ in range(n):
    security_list.append(input())
castle_row = [0]*n
castle_column = [0]*m

for i in range(n):
    for j in range(m):
        if security_list[i][j] == 'X':
            castle_row[i] += 1
            castle_column[j] += 1
castle_zero_row = 0

#=================================== 여기까지는 ok.
for row in castle_row:
    if row == 0:
        castle_zero_row += 1
castle_zero_column = 0

for col in castle_column:
    if col == 0:
        castle_zero_column += 1


print(max(castle_zero_row, castle_zero_column))

# 어렵다...ㅠㅠ