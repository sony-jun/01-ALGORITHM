V = int(input()) # 정점의 수
E = int(input()) # 간선의 수

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
total = 0

# 인접 리스트 만들기
for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
    start = 1
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
print(visited)