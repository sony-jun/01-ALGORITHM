import sys
sys.stdin = open("75_누울 자리를 찾아라_1652.txt", "r")

# 정방향 순회하며 cnt += 1
# cnt == 2 되면 break result += 1

# 왼쪽으로 90' 돌린 매트릭스, 순회하며 cnt += 1
# cnt == 2 되면 break result += 1

N = int(input())

matrix = [] # ['....X', '..XX.', '.....', '.XX..', 'X....']
for i in range(N):
    matrix.append(input())

x_result = 0
for i in range(N):
    x_cnt = 0
    for j in range(N):

        if matrix[i][j] == ".":
            x_cnt += 1
        else:
            x_cnt = 0
            
        if x_cnt == 2:
            x_result += 1


y_result = 0
for a in range(N):
    y_cnt = 0
    for b in range(N):

        if matrix[b][a] == ".":
            y_cnt += 1
        else:
            y_cnt = 0

        if y_cnt == 2:
            y_result += 1


print(x_result, y_result)