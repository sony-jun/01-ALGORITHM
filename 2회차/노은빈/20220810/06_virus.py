'''graph = [
    [2,5],
    [1,3,5],
    [2],
    [7],
    [1,2,6],
    [5],
    [4]
]'''
n = int(input()) #정점 개수(컴퓨터 수)
m = int(input()) #간선 개수(네트워크 수)

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

#인접리스트 만들기
for _ in range(m) :
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack :
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)
print(visited.count(True) - 1)