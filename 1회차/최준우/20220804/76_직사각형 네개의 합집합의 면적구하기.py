# https://www.acmicpc.net/problem/2669

coordinate = [[0] * 100 for _ in range(100)]

for c in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2-1+1):
        for j in range(y1, y2-1+1):
            coordinate[i][j] = 'x'

result = 0
for x in range(100):
    for y in range(100):
        if coordinate[x][y] == 'x':
            result += 1
print(result)

