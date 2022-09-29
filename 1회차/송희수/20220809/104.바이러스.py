import sys

sys.stdin = open("104.바이러스.txt")

N = int(input())
M = int(input())


graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph2[u].append(v)
    graph2[v].append(u)

print(graph2)