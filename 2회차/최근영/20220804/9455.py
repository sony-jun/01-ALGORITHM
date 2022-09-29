import sys

N = int(sys.stdin.readline())

for i in range(1,N+1):
    n,m = list(map(int,sys.stdin.readline().split()))
    matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    print(matrix)