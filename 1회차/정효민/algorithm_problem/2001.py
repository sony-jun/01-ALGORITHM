
from pprint import pprint
import sys


sys.stdin = open('2001.txt')
n,m = map(int , input().split())
mat = []
z = []

for _ in range(n):
    line = list(map(int , (input().split())))
    mat.append(line)
for x in range(n - m + 1):
    
    for y in range(n - m + 1):
        result = 0
        for i in range(x , x + m):
            for j in range(y , y + m):
                result = result + mat[i][j]
        z.append(result)            

       
        # pprint(result)
print(max(z))