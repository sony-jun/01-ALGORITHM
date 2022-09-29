n = int(input())
e = int(input())
graph_list = [[] for _ in range(n+1)]
visited = [False]* (n+1)
for _ in range(e):
    
    u,v = map(int,input().split())

    graph_list[u].append(v)
    graph_list[v].append(u)

# dfs code
def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph_list[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)
print(sum(visited)-1)