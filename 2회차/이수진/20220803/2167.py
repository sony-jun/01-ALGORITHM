import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arrs = [list(map(int,input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
    i,j,x,y = map(int, input().split()) #1 1 2 3
    result = 0 
    for a in range(i-1, x): #0 2
        for b in range(j-1, y): #0 3
            result += arrs[a][b]
    print(result)