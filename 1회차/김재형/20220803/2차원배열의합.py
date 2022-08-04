import sys
sys.stdin = open('2차원배열의합_input.txt')

N ,M = map(int, input().split())

A = [] #[[1, 2, 4], [8, 16, 32]]
for _ in range(N):
    A.append(list(map(int, input().split())))

# K번 실행
K = int(input())

for k in range(K):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    sum_ = 0
    for r in range(i, x+1):
        for c in range(j,y+1):
            sum_ += A[r][c]
    print(sum_)

