import sys
sys.stdin = open('1652.txt')

N = int(sys.stdin.readline())
room = [list((sys.stdin.readline().rstrip())) for _ in range(N)]
r, c = 0, 0

for x in range(N):
    for y in range(N-1):
        if room[x][y:y+2] == ['.', '.']:
            r += 1
            break
for y in range(N):
    for x in range(N-1):
        if room[x][]
print(r,c)