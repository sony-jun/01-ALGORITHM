import sys 
sys.stdin = open('B11724.txt')

V, E = map(int, input().split())
graph = [[] * (V+1) for _ in range(V+1)]
for _ in range(E): 
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)
