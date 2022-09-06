
import sys


sys.stdin = open('bj1231.txt')

c , d , m = map(int , input().split())

mat = []


for i in range(c):
    line = list(input().split())
    mat.append(line)

for x in range(c):
    for y in range(d):
        if x + 1 <= d:
            if  mat[x][y] > mat[x + 1][y]:
                print('1')
            else:
                print('2')
        
