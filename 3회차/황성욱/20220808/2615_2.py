import sys
from pprint import pprint

sys.stdin = open('./2615.txt')
matrix = [list(map(int, input().split())) for _ in range(19)]


dx = [1, 1, 0, 1]
dy = [0, 1, 1, -1]

res = False

for i in range(19):
    for j in range(19):
        if matrix[i][j] == 1 or matrix[i][j] == 2:
            for d in range(4): # 방향 벡터
                cnt = [0, 0, 0, 0] # cnt 배열
                nx = j
                ny = i
                for dir in range(4): # 4번 반복 << 오목
                    nx += dx[d]
                    ny += dy[d]
                    
                    if 0 <= nx <= 18 and 0 <= ny <= 18:
                        if matrix[i][j] == matrix[ny][nx]:
                            cnt[d] += 1
                        
                        if cnt[d] == 4:
                            if 0 <= ny + dy[d] <= 18 and 0 <= nx + dx[d] <= 18: 
                                if matrix[ny + dy[d]][nx + dx[d]] == matrix[i][j]:
                                    break
                            if 0 <= i - dy[d] <= 18 and 0 <= j - dx[d] <= 18:
                                if matrix[i - dy[d]][j - dx[d]] == matrix[i][j]:
                                    break
                            res = True
                            print(matrix[i][j])
                            print(i + 1, j + 1)
if not res:
    print(0)              

            
