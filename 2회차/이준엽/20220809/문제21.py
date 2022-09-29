n,m = map(int,input().split())
ajcoord = [list(0 for i in range(n+1)) for i in range(n+1)]
ajlist = [[]for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    ajcoord[u][v] = 1
    ajcoord[v][u] = 1
    ajlist[u].append(v)
    ajlist[v].append(u)
print(ajcoord,ajlist,sep='\n')