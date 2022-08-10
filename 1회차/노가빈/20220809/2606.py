n = int(input()) # 정점 개수(컴퓨터)
m = int(input()) # 간선 개수(네트워크)
graph = [[] for _ in range(n + 1)]
# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
#print(graph)

visited = [False] * n
def dfs(start):
    count = 0   
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                count += 1
                stack.append(adj)
    print(count)
dfs(1)