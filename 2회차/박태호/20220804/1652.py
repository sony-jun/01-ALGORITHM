# 누울자리 찾기
# 각 빈칸의 최대값을 출력하면 될듯하다.
import sys
from pprint import pprint
sys.stdin = open('누울자리.txt','r')
n = int(input())
mat = [list(input()) for _ in range(n)]
# pprint(mat)
max_x = 0
max_y = 0
li=[]
for i in range(n):
    r=[]
    cnt =0 
    for j in range(n):
        if mat[i][j] == '.':
            cnt += 1
            
        else:
            if cnt >= 2:
                max_x += 1
            
            cnt = 0
    if cnt > 1:
        max_x += 1
    
    cnt =0 
    for j in range(n):
        if mat[j][i] == '.':
            cnt += 1
            
        else:
            if cnt >= 2:
                max_y += 1
            
            cnt = 0
    if cnt > 1:
        max_y += 1
    

    #     r.append(mat[j][i])
    # li.append(r)
print(max_x,max_y)
# pprint(li)