import sys
from pprint import pprint

sys.stdin = open("0_성지키기.txt", 'r')

castle = []

row = []
column = []

need = 0

N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    row.append(False)
    
for j in range(M):
    column.append(False)

for floor in range(N):
    castle.append(list(sys.stdin.readline().rstrip()))
    
    if 'X' in castle[floor]:
        row[floor] = True
        
    for room in range(M):
        if castle[floor][room] == 'X':
            column[room] = True

need_row = row.count(False)
need_column = column.count(False)

print(need_row if need_row >= need_column else need_column)