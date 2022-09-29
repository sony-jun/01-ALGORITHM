from pprint import pprint 
import sys
sys.stdin = open("6. 무방향 그래프 표현하기.txt", "r")

input = sys.stdin.readline

N,M = map(int,input().split())

# 인접 행렬 만들기

graph = [[0] * N for _ in range(N)]
graph2 = [[] for _ in range(N)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    graph2[v1].append(v2)
    graph2[v2].append(v1)



pprint(graph)
print(graph2)
