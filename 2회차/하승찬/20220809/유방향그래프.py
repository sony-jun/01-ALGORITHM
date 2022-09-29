# > 그래프 입력이 주어질 때 `유방향` 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 `정점의 개수 N`과 `간선의 개수 M`이 주어진다.  둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.
# > 
from pprint import pprint
n,m= map(int,input().split())

n+= 1
graphm= [[0]*n for __ in range(n)]

graphl= [[] for __ in range(n)]


for __ in range(m):
    u,v = map (int,input().split())
    graphm[u][v] = 1
    graphl[u].append(v)

pprint(graphm)
pprint(graphl)
