from sqlite3 import Row
import sys

sys.stdin = open("69_성지키기.txt")

n, m = map(int, input().split())

list_=[]

for tc in range(n):
    list_.append(input())

row_count, col_count = 0, 0

# 행만 세는 코드
for i in range(n):
    if 'X' not in list_[i]:
        row_count += 1

# 열만 세는 코드
for j in range(m):
    if 'X' not in [list_[i][j] for i in range(n)]:
        col_count += 1
print(max(row_count, col_count))

