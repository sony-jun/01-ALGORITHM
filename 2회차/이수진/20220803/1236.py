import sys
input = sys.stdin.readline

n,m=map(int, input().split())
castle = [input() for _ in range(n)]
need_rowguard=0
need_columnguard=0

for floor in castle: # 행 탐색
    if 'X' not in floor:
        need_rowguard += 1

for room in range(m): # 열 탐색
    temp=''
    for floor in range(n):
        temp+=castle[floor][room]
    if 'X' not in temp:
        need_columnguard += 1    

print(need_rowguard if need_rowguard>=need_columnguard else need_columnguard)