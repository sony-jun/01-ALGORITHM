import sys
sys.stdin = open("미로탐색.txt", "r")

i, j = map(int, input().split())
seet = []
for _ in range(i):
    line = list(str(input()))
    seet.append(line)
# print(seet)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

cnt = 0

point = [0, 0]
turn = 0
passed = [point]

while point != [i, j]:
    for _ in range(4):
        ni = point[0] + di[_]
        nj = point[1] + dj[_]
        while ni in range(i) and nj in range(j) and seet[ni][nj] == '1':
            if [ni, nj] in passed:
                break
            passed.append([ni, nj])
            cnt += 1
            point = [ni, nj]
            ni += di[_]
            nj += dj[_]
        turn += 1
        if turn % 4 == 0:
            point = [-1 * (turn//4) -1]
            cnt -= 1
    # else:
print(cnt, turn, point)