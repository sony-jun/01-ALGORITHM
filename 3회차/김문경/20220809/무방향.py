from pprint import pprint
n, m = map(int, input().split())

#* 1. 인접 행렬
graph = [[0] * (n + 1) for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
pprint(graph)

#* 2. 인접 리스트
# 정점 개수만큼 빈 리스트 공간을 만들어서 전체 graph 리스트에 넣기
graph = [[] for _ in range(n + 1)]

# 간선 횟수 만큼 반복해주기
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)
    