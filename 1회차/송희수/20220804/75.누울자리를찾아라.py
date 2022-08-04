import sys

import sys

sys.stdin = open("75.누울자리를찾아라.txt")

N = int(input())

matrix = [list(map(str, input())) for tc in range(N)]


ans = [0,0]
for i in range(N):
    leng_r,leng_c = 0,0 # 가로 길이, 세로 길이 각각을 나타낸다.
    for j in range(N):
        # 가로
        if matrix[i][j] == '.':
            leng_r+=1
        else:
            leng_r=0
        if leng_r==2:
            ans[0] += 1
        
        # 세로
        if matrix[j][i] == '.':
            leng_c+=1
        else:
            leng_c=0
        if leng_c==2:
            ans[1] += 1
print(ans[0], ans[1], end = " ")
