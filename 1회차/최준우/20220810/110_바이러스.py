# https://www.acmicpc.net/problem/2606

N = int(input())
direct_connection = int(input())
adjacency_list = [[] for _ in range(N+1)]

for _ in range(direct_connection):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

cnt = 0
visited = [0] * (N + 1)
def dfs(start):
    global cnt
    visited[start] = 1
    
    for i in adjacency_list[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)