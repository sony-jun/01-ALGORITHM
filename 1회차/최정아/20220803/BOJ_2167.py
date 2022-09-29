import sys
input = sys.stdin.readline

# 행렬의 크기 입력으로 주어짐
n, m = map(int, input().split())
# List Comprehension 사용해서 이차원 리스트 입력 받음
matrix = [list(map(int,input().split())) for _ in range(n)]

cnt = int(input())
for k in range(cnt):
    mum = 0
    i, j, x, y = map(int,input().split())
    
    for w in range(i-1,x):
        for v in range(j-1,y):
            mum += matrix[w][v]
    print(mum)