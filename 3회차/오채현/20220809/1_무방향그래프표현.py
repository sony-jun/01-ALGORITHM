from pprint import pprint

# n, m = 6, 5
# n: 정점의 개수 m:간선의 개수


# pprint(graph)
n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

    graph2[v1].append(v2)
    graph2[v2].append(v1)

pprint(graph)
pprint(graph2)


# graph2 = [[] for _ in range(n+1)]

# for j in range(m):
#     v1, v2 = map(int, input().split())
#     graph2[v1].append(v2)
#     graph2[v2].append(v1)

# pprint(graph2)
