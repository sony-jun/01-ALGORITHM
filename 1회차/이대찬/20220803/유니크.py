import sys

sys.stdin = open('유니크.txt')

N = int(input())

matrix = [list(map(int,(input().split()))) for _ in range(N)] #매트릭스 원소 입력

result = [[0]*3 for _ in range(N)]

for i in range(N):
    for n in range(3):
        result[i][n] = matrix[i][n]

for n in range(N):  # 행 
    for i in range(3):  # 열
        for k in range(0,N):  #열 원소값 비교
            if k == n:
                continue  
            if matrix[n][i] == matrix[k][i]:
                result[n][i] = 0 
                break
 
for i in result:
    print(sum(i))
    
