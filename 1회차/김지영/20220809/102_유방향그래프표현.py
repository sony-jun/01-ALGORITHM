def ppr(lst):
    for i in lst:
        print(i,end='\n')

node, edge = map(int,input().split()) # 5,6

graph_matrix = [[0]*(node+1) for _ in range(node+1)]
graph_list = [[]*(node+1) for _ in range(node+1)]

for _ in range(edge):
    
    u,v = map(int,input().split())
    
    graph_matrix[u][v] = 1

    graph_list[u].append(v)
    
ppr(graph_matrix)
print(graph_list)