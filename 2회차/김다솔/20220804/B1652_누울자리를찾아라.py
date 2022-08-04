import sys
sys.stdin = open('B1652.txt')
# N = int(sys.stdin.readline())
# room = [list(sys.stdin.readline()) for _ in range(N)]
N = int(input())
room = [list(input()) for _ in range(N)]
# print(room)

r = 0
c = 0
cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            r += 1
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            c += 1
print(r, c)