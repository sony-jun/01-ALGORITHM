# https://www.notion.so/hphk-edu/21-bb38e88c331a46628d5c6ee33ddcd50c

N, M  = map(int,input().split())
adj_lst = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    adj_lst[u][v] = 1
    adj_lst[v][u] = 1
print(adj_lst)