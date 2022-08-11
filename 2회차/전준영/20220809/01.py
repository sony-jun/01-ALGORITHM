import sys
input=sys.stdin.readline
N,M=map(int,input().split())
array=[[] for _ in range(N+1)]
metrix=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    array[a].append(b)
    metrix[a][b]=1
print(array)
print(metrix)
    