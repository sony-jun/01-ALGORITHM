import sys
sys.stdin = open('2차원배열의합.txt','r')
from pprint import pprint
input = sys.stdin.readline

N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
#pprint(matrix)
K = int(input())

for _ in range(K):
    i, j, x, y = map(int,input().split())
    sum_ = 0
    for a in range(i-1,x):
        for b in range(j-1,y):
            sum_ += matrix[a][b]
    print(sum_)