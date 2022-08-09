# 그래프의 입력이 주어질 때
# 무방향 그래프를 인접행렬
# 인접리스트로 표현
# 두번째 줄 부터 간선의 양 끝점 u, v가 주어짐

# 인접행렬 
# n, m = map(int, input().split())

# graph = [[0] * (n+1) for _ in range(n+1)] # 정점 갯수 만큼 반복해서 0 행렬 배열 만듬

# for _ in range(m): # 간선 갯수만큼 반복
#     v1, v2 = map(int, input().split()) # 
#     graph[v1][v2] = 1 # [1], [2]
#     graph[v2][v1] = 1 # [2], [1]

# print(graph)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 인접 리스트
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)] 

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)
