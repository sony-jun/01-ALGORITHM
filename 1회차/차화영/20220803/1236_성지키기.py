import sys
sys.stdin = open("1236.txt", "r")

N, M = map(int, input().split())
matrix = []

for _ in range(N):
    line = list(input())
    matrix.append(line)

row = 0 # 행에 필요한 경비원의 수 
col = 0 # 열에 필요한 경비원의 수 

for i in range(N): # 행 체크
    if "X" not in matrix[i]:
        row += 1
for j in range(M): # 열 체크
    if "X" not in [matrix[i][j] for i in range(N)]:
        col += 1
print(max(row, col)) # row와 col 값 중 큰 값을 출력 -- 행에 3명이 필요하고 열에 1명이 필요하면 3명의 경비원이 필요한 것.