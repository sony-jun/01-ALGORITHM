from pprint import pprint

n, m = map(int,input().split())

# 인접 행렬 만들기
graph = [[0]*(n+1) for _ in range(n+1)]
# 인접 리스트 만들기
list_ = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    list_[x].append(y)
    list_[y].append(x)

pprint(graph)
pprint(list_)

