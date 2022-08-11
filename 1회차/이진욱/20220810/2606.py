def dfs(visted, x, graph):
    visted[x] = True # x = 1

    for i in graph[x]: # i = 2,5
        if visted[i] != True : # 방문체크에서 2 -> False
            dfs(visted, i, graph) #  dfs(visted,2,graph)

# ---------------------------------------------------------------------------------------------

N = int(input())
M = int(input())

org_list = [[ 0 for _ in range(N+1) ] for _ in range(N+1)    ]

for i in range(M):
    u,v = map(int,input().split())
    org_list[u][v] = 1
    org_list[v][u] = 1

ad_list = [[ 0 for _ in range(N+1) ] for _ in range(N+1)    ]

for i in range(N+1):
    ad_list[i] = [ k for k in range(N+1) if org_list[i][k] == 1    ] # 인접 리스트

# ---------------------------------------------------------------------------------------------

visted = [0]*(N+1) # 방문여부 체크

print(ad_list)

dfs(visted,1,ad_list)


true_list = [ i for i in visted if i == True  ]

print(visted)
print(len(true_list)-1)

                 
