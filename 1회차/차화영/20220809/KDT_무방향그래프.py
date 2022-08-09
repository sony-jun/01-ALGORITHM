import sys
from pprint import pprint

input = sys.stdin.readline

n, m = map(int, input().split()) # 정점의 개수 n, 간선의 개수 m

list_1 = [[0] * (n + 1) for _ in range(n + 1)] # n+1 * n+1의 크기의 행렬을 0으로 초기화
list_2 = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    list_2[a].append(b)
    list_2[b].append(a)

    list_1[a][b] = 1
    list_1[b][a] = 1

pprint(list_1)
print(list_2)
