N, M = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
list_ = [[] for _ in range(N+1) ]
for i in range(M):
    p1, p2 = map(int,input().split())
    graph[p1][p2] = 1
    graph[p2][p1] = 1
    
    list_[p1].append(p2)
    list_[p2].append(p1)


print(graph)
print(list_)