from pprint import pprint


N,M = map(int,input().split())


# 인접 행렬
j = [[0]*(N+1) for _ in range(N+1)]

# 인접 리스트
list = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int,input().split())
    
    j[u][v] = 1 # n1과 n2 인접
    j[v][u] = 1 # 방향 표시가 없는 경우

    list[u].append(v)
    list[v].append(u)


pprint(j)
pprint(list)

