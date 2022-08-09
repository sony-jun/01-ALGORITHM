
# 인접행렬 


# n, m = map(int, input().split())
# graph = [[0] * (n+1) for _ in range(n+1)]

# for _ in range(m): # 간선 갯수만큼 반복
#     v1, v2 = map(int, input().split()) # 
#     graph[v1][v2] = 1 # [1], [2]

# print(graph)



# 인접 리스트
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)] 

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

print(graph)
