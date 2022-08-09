from pprint import pprint

n, m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
list_ = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    list_[x].append(y)

pprint(graph)
pprint(list_)