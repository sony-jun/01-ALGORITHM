from re import L
import sys
sys.stdin = open("26_성지키기.txt")

n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(input())

row = 0
col = 0

for i in li:
    if not 'X' in i:
        row += 1
        
for i in range(m):
    if not 'X' in [li[j][i] for j in range(n)]:
        col += 1
print(max(row, col))