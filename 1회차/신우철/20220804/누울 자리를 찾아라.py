# 1652
import sys

sys.stdin = open('누울 자리를 찾아라.txt')
N = int(input())
matrix = [list(input()) for _ in range(N)]
x=0
y=0


for i in range(N):
    a = 0 
    b = 0
    for j in range(N):
        if matrix[i][j] == '.' :
            a += 1
        else:
            a = 0
        if a == 2:
            x += 1

        if matrix[j][i] == '.' :
            b += 1
        else:
            b = 0
        if b == 2 :
            y += 1
                
print(x,y)





        
        
