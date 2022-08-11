import sys 
sys.stdin = open('B11724.txt')

V, E = map(int, input().split())
graph = [[] * (V+1) for _ in range(V+1)]
for _ in range(E): 
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)

#모든노드에서 출발을 해볼건데 
#시작을 한 횟수 ? 
ans = 0
for start in range(1, n + 1):
    if not visited[start]:
        
    