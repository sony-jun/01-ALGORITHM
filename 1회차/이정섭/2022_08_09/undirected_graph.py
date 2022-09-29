node, edge = map(int,input().split())

u_graph = []
adj = [[]*(node + 1) for i in range(node + 1)]

for i in range(node + 1):
    for j in range(node + 1):
        if u_graph[i][j] == 1:
            adj[i].append[j]

print(adj)

for i in range(node + 1):
    u_graph.append([0] * (node + 1))

for i in range (edge):
    start, end = map(int, input().split())  
    u_graph[start][end] = 1
    u_graph[end][start] = 1

print(u_graph)  