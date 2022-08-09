# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open('B2606.txt')
V = int(input())
E = int(input())
network = [[] * (V+1) for _ in range(V+1)]

for _ in range(E):
    v1, v2 = map(int, input().split())
    network[v1].append(v2)
    network[v2].append(v1)
# print(network)
cnt = 0 
