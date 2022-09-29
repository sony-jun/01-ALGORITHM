import sys

input = sys.stdin.readline

n = int(input())

maps = [list(input().rstrip()) for _ in range(n)]
maps2 = list(map(list, zip(*maps)))

row, col = 0, 0
for i in range(n):
    cnt1 = 0
    for j in range(n):
        if maps[i][j] == ".":
            cnt1 += 1
        else:
            if cnt1 >= 2:
                row += 1
            cnt1 = 0
    if cnt1 >= 2:
        row += 1
for i in range(n):
    cnt2 = 0
    for j in range(n):
        if maps2[i][j] == ".":
            cnt2 += 1
        else:
            if cnt2 >= 2:
                col += 1
            cnt2 = 0
    if cnt2 >= 2:
        col += 1
print(row, col)
##############
n = int(input())
matrix = [list(input()) for _ in range(n)]

sleep_1 = 0
sleep_2 = 0

for y in range(n):
    count_1 = 0
    for x in range(n):
        if matrix[x][y] == '.':
            count_1 += 1
        elif matrix[x][y] == 'X':
            if count_1 >= 2:
                sleep_1 += 1
            count_1 = 0
    if count_1 >= 2:
        sleep_1 += 1

for x in range(n):
    count_2 = 0
    for y in range(n):
        if matrix[x][y] == '.':
            count_2 += 1
        elif matrix[x][y] == 'X':
            if count_2 >= 2:
                sleep_2 += 1
            count_2 = 0
    if count_2 >= 2:
        sleep_2 += 1

print(sleep_2, sleep_1)