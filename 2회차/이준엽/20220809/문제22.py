n,m = map(int,input().split())
ajcoord = [list(0 for i in range(n+1)) for i in range(n+1)]
ajlist = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    ajcoord[u][v] = 1
    ajlist[u].append(v)
print(ajcoord,ajlist,sep='\n')