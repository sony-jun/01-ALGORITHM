#9455
import sys

sys.stdin = open('박스.txt')
a = int(input())
for _ in range(a):
    M,N = map(int,input().split())
    matrix = [[] for _ in range(N)]
    for i in range(M):
        a = list(input().split())
        for j in range(N):
            matrix[j].append(a[j])
            
    cnt = 0
    for i in range(N):
        boxsu = matrix[i].count('1')
        floor = M - 1
        
        for j in range(M -1,-1,-1):
            if matrix[i][j] == '1':
                cnt += floor - j
                floor -= 1
                
    print(cnt)