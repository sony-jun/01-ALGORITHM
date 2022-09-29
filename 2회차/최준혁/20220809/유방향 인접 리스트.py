N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
print(adj_list)
