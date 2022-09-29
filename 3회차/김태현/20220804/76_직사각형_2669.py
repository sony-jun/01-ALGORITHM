import sys
sys.stdin = open("76_직사각형_2669.txt", "r")

# 점 좌표가 아니라, 박스 좌표라고 생각
# a, b가 주어지면, range(a, b+1) 범위가 아닌, range(a, b +1 -1)을 순회
# 주어진 범위를 순회하며, 각 위치에 += 1

# 100 x 100 매트릭스 생성
matrix = [[0] * 100 for _ in range(100 + 1)]

# i, j, x, y
cnt = 0
for i in range(4):
    i, j, x, y = map(int, input().split())
    for a in range(i, x): # range(i, x+1)이 아닌 이유: 좌표가 아니라 박스를 구해야 해서
        for b in range(j, y):
            if matrix[a][b] == 0:
                matrix[a][b] += 1
                cnt += 1

print(cnt)