n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for t in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * n

# dfs 탐색
def dfs(start):
    stack = [start]
    visited[start] = 1

    while stack:
        cur = stack.pop()

        for i in graph[cur]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
    # 방문한 컴퓨터의 총 합계 출력
    print(sum(visited)-1)

dfs(1)