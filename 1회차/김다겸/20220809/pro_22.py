from pprint import pprint
n, m = map(int, input().split())

graph = [list([0] * 7) for _ in range(7)]
list_ = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    list_[u].append(v)

pprint(graph)
print(list_)