from pprint import pprint
u,v = map(int, input().split())

graph = [[0] *  (u+1) for _ in range(u+1)]
adj_list = [[] for _ in range(u+1)]
for a in range(v):
    x,y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
    graph[x][y] = 1
    graph[y][x] = 1

pprint(graph)
pprint(adj_list)