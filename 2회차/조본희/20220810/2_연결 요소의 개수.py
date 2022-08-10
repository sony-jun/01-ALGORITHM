import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

N, M = map(int, input().split())
N += 1

graph = [[] for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * N
cnt = 0

for j in range(1, N):
    if not visited[j]:
        if not graph[j]:
            cnt += 1
            visited[j] = 1
        else:
            dfs(j)
            cnt += 1

print(cnt)