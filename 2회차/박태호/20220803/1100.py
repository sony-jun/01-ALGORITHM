# 하얀 칸
# 0,0 = 하얀칸
from pprint import pprint
import sys
sys.stdin = open('하얀칸.txt','r')
mat = [list(input()) for _ in range(8)]
# pprint(mat)
cnt = 0 
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if mat[i][j] == 'F':
                cnt += 1
print(cnt)