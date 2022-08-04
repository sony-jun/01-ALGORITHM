from doctest import master
import sys

sys.stdin = open('박스.txt')

N = int(input())

for i in range(N):
    m,n = map(int,(input().split()))
    matrix = [list((input().split())) for _ in range(m)]
    
    cnt =0
    for c in range(n):
        while(1):
            T = 0
            for r in range(1,m):
            
                if  matrix[r-1][c] ==1 and matrix[r][c] ==0:
                    matrix[r-1][c] =0 
                    matrix[r][c] =1
                    print(matrix)
                    cnt +=1
                    T +=1
            if T == 0:
                break    
            
    print(cnt)
            

 