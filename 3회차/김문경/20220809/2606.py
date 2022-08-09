from pprint import pprint
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

virus = [1]
while True:
    for i in virus:
        if i not in virus:
            virus.append(graph[i])
