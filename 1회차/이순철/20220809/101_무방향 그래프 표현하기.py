from pprint import pprint
import sys
sys.stdin = open('_무방향 그래프 표현하기.txt')

n, m = map(int, input().split())
pan = [[0] * (n) for _ in range(n)]
# 인접 행렬
point = [[] for _ in range(n)]
# 인접 리스트

for _ in range(m):
    u, v = map(int, input().split())
    # 인접 행렬에 값을 넣음
    pan[u][v] = 1
    pan[v][u] = 1
    # 인접 리스트에 값을 넣음
    point[u].append(v)
    point[v].append(u)

pprint(pan)
print(point)