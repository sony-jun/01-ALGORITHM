n, m = map(int, input().split())
#인접행렬
graph = [[0]* (n+1) for _ in range(n+1)]

#간선의 개수 만큼 돌아주면서
for _ in range(m):
    u, v = map(int, input().split())
    #Graph에서 u,v에 해당하는 인덱스에 1을 넣어준다. 
    graph[u][v] = 1
    graph[v][u] = 1
print(graph)

n, m = map(int, input().split())
#인접리스트
graph = [[]* (n+1) for _ in range(n+1)]

#간선의 개수 만큼 돌아주면서
for _ in range(m):
    u, v = map(int, input().split())
    #각각 Graph의 u, v에 해당하는 인덱스에 v, u를 넣어준다.
    graph[u].append(v) 
    graph[v].append(u)

print(graph)
