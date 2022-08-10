
N,M = map(int,input().split())

org_list = [[ 0 for _ in range(N+1) ] for _ in range(N+1)    ]

for i in range(M):
    u,v = map(int,input().split())
    org_list[u][v] = 1
    org_list[v][u] = 1

ad_list = [0]*(N+1)

for i in range(N+1):
    ad_list[i] = [ k for k in range(N+1) if org_list[i][k] == 1    ]

print(org_list)
print(ad_list)