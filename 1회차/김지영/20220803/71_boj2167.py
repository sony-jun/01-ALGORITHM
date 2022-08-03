n,m = map(int,input().split())
dlst = [list(map(int,input().split())) for _ in range(n)]
# print(dlst)
k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    result = 0
    for n in range(i-1,x):
        for m in range(j-1,y):
            result += dlst[n][m]
    print(result)