from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]: # i = 1차원의 요소
        if not visited[i]: # 방문하지 않았다면
            print(visited)
            dfs(graph, i, visited) # 다시 dfs               

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
print(dfs(graph, 1, visited))
