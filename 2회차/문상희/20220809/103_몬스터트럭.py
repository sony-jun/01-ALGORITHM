area = list(map(int, input().split()))
matrix = []
for i in range(area[0]):
    line = list(input())
    matrix.append(line)
di = [0, 1, 1, 0]
dj = [0, 0, 1, 1]

broken = [0, 0, 0, 0, 0] 
for i in range(area[0] - 1):
    for j in range(area[1] - 1):
        cnt = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni in range(area[0]) and nj in range(area[1]):
                if matrix[ni][nj] =='#':
                    break
                elif matrix[ni][nj] =='X':
                    cnt += 1
        else:
            broken[cnt] += 1

for i in broken:
    print(i)