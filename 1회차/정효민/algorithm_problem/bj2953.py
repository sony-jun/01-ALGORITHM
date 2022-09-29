from operator import index
import sys


sys.stdin = open('bj2953.txt')
mat = []
result =[]
for i in range(5):
    line = list(map(int ,input().split()))
    mat.append(line)
    
for x in range(5):
    result.append(sum(mat[x]))
print(max(result) , result.index(max(result)) + 1)
    
    

