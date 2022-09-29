# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 
import sys

N, M = map(int,input().split())
m=[]
sum_num = 0
for i in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    m.append(a)
K = int(input())
for k in range(K):
    i,j,x,y = map(map(int,sys.stdin.readline().split()))
for c in range(i-1,x):
    for r in range(j-1,y):
        sum_num+=m[c][r]
print(sum_num)