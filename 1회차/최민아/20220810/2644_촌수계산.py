import sys
sys.setrecursionlimit(10000)            # 재귀횟수 지정
sys.stdin = open("20220810/2644_촌수계산.txt")

n = int(input())
a, b = map(int, input().split())
m = int(input())

family = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)