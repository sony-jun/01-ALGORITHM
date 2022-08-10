# https://www.acmicpc.net/problem/2644

from pprint import pprint

n = int(input())
person1, person2 = map(int, input().split())
m = int(input())

adjacency_matrix = [[0] * (n+1) for _ in range(n+1)]
adjacency_list = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adjacency_matrix[u][v] = 1
    adjacency_matrix[v][u] = 1
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
pprint(adjacency_matrix)
print(adjacency_list)

cnt = 0
result = 0
visited = [0] * (n + 1)
def dfs(start):
    global cnt
    global result
    visited[start] = 1
    for i in adjacency_list[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
        if start == person2:
            result = cnt
dfs(person1)
print(result)