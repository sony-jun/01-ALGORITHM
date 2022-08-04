# 누울 자리를 찾아라 🐳
# 문제 : 연속해서 2칸 이상의 빈 칸이 누울 자리(반드시 벽이나 짐에 닿음)
# 출력 : 첫째 줄에 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력

n = int(input())

room = [list(input()) for _ in range(n)]

row = 0
for x in range(n):
    cnt = 0
    for y in range(n):
        if room[x][y] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row += 1

col = 0
for x in range(n):
    cnt = 0
    for y in range(n):
        if room[y][x] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            col += 1

print(row, col)
