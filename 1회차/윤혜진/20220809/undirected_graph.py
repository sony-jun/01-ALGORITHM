# 문제.무방향 그래프 표현하기



# 문제 내용
'''
그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
인접 행렬을 출력하고, 인접 리스트를 출력하세요.
'''


# 코드 1 - 인접 행렬 출력
import sys
from pprint import pprint

sys.stdin = open('input_text/undirected_graph.txt')

N, M = map(int, input().split())

# 인접 행렬 만들기
graph = [[0] * (N + 1) for _ in range(N + 1)]   # 정점: 1 ~ N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

pprint(graph)



# 코드 2 - 인접 리스트 출력
import sys
from pprint import pprint

sys.stdin = open('input_text/undirected_graph.txt')

N, M = map(int, input().split())

# 인접 리스트 만들기
graph = [[] for _ in range(N + 1)]   # 인덱스: 1 ~ N 정점, 값: 각 정점의 인접 정점
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)