#성 지키기
from pprint import pprint
import sys
sys.stdin = open('성지키기.txt','r')

n, m = list(map(int,input().split()))
matrix = []
matrix = [list(input()) for _ in range(n)]
# pprint(matrix)
cntx = 0
cnty = 0
for i in range(n):
    # print(i)
    if 'X' not in matrix[i]: 
        cntx += 1 #  행의 빈칸


for j in range(m): # 0
    li=[]
    # print(matrix[i][j])
    for i in range(n): #행 0~3
        li.append(matrix[i][j])
    if 'X' not in li:
        # print(li)
        cnty += 1
print(max(cnty,cntx))
