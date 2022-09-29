from pprint import pprint
import sys
sys.stdin = open('_유방향 그래프 표현하기.txt')

n, m = map(int, input().split())
pan = [[0] * (n) for _ in range(n)]
# 인접 행렬
point = [[] for _ in range(n)]
# 인접 리스트

for _ in range(m):
    u, v = map(int, input().split())
    pan[u][v] = 1
    point[u].append(v)

pprint(pan)
print(point)