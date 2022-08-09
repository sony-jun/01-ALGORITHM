from pprint import pprint
n, m = map(int, input().split())

#* 1. 인접 행렬
graph = [[0] * (n + 1) for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    # v1에서 v2는 가능하지만, v2에서 v1은 불가능하므로
    # graph[v1][v2]에서만 간선 추가
pprint(graph)

#* 2. 인접 리스트
# 정점 개수만큼 빈 리스트 공간을 만들어서 전체 graph 리스트에 넣기
graph = [[] for _ in range(n + 1)]

# 간선 횟수 만큼 반복해주기
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
print(graph)