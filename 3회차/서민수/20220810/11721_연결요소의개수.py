# 방향 없는 그래프가 주어졌을 때, 
# 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
#  둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#  (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

from pprint import pprint


N,M = map(int,input().split())


# 인접 행렬
j = [[0]*(N+1) for _ in range(N+1)]

# 인접 리스트
list = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int,input().split())
    
    j[u][v] = 1 # n1과 n2 인접
    j[v][u] = 1 # 방향 표시가 없는 경우

    list[u].append(v)
    list[v].append(u)


pprint(j)
pprint(list)

