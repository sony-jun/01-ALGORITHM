import sys
sys.stdin = open("1_누울자리를찾아라.txt")

N = int(input())
room = []


for _ in range(1, N+1):
    room.append(input())

cnt = 0
row = 0
col = 0

for i in range(N):
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt > 1:
                row += 1
            cnt = 0
    if cnt > 1:
        row += 1
    cnt = 0
        
for i in range(N):
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        else:
            if cnt > 1:
                col += 1
            cnt = 0
    if cnt > 1:
        col += 1
    cnt = 0

print(row, col)

