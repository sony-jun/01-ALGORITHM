# 2669
import sys

sys.stdin = open('직사각형.txt')
matrix = [[ 0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(x1,x2):
        for j in range(y1, y2):
            matrix[i][j] = 1
a = 0      
for z in matrix:
    a += sum(z)
print(a)