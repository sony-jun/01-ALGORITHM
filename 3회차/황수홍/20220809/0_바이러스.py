N= int(input()) # 컴퓨터의 수
link = int(input()) # 컴퓨터 쌍의 수

network = [[]*(N+1) for _ in range(N+1)]

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
print(network)
visited = [0] * (N+1)	# 방문처리 : 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True

dfs(network, 1, visited)
print(sum(visited)-1)