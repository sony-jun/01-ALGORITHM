import sys
input = sys.stdin.readline

# dfs 탐색
def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 인접 리스트 생성
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# visited 리스트 생성
visited = [False] * (n + 1)
count = 0

for j in range(1, n+1):
    # 방문하지 않았다면
    if not visited[j]:
        # 그 값으로 dfs
        dfs(j)
        # count에 1 더하기
        count += 1
print(count)