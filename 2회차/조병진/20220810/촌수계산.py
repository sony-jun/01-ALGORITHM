# 촌수계산 🐳
# 문제 : 여러 사람에 대한 관계가 주어질 때, 두사람 간의 촌수 구하기

T = int(input())
N, M = map(int, input().split())
J = int(input())

JOIN = [[] for _ in range(T + 1)]

for i in range(J):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (T + 1)


def DFS(v):
    for i in JOIN[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            DFS(i)


DFS(N)
if visited[M] > 0:
    print(visited[M])
else:
    print(-1)
