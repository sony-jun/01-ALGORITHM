import sys
from pprint import pprint 
sys.stdin = open("7. 유방향 그래프 표현하기.txt", "r")

input = sys.stdin.readline

N , M = map(int,input().split())

graph = [[0] * N for _ in range(N)]
graph2 = [[] for _ in range(N)]
for i in range(M):
    v1 , v2 = map(int,input().split())
    graph[v1][v2] = 1
    if v1 == 5 and v2 == 1:
        graph[v2][v1] = 1
    graph2[v1].append(v2)     
pprint(graph)
print(graph2)