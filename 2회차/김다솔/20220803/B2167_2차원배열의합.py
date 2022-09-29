import sys
sys.stdin = open('B2167.txt')

N, M = map(int, input().split())
nm = [list(map(int, input().split())) for _ in range(N)]
# print(nm)

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum_ = 0
    
    for r in range(i-1, x):
        for c in range(j-1, y):
            sum_ += nm[r][c]
        
    print(sum_)

#pypy3만 통과, python3은 시간초과