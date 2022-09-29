from pprint import pprint
n, m = map(int, input().split())
list_1 = [[0]*(n+1) for _ in range(n+1)]
list_2 = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    list_1[u][v] = 1
    list_2[u].append(v)
pprint(list_1)
pprint(list_2)