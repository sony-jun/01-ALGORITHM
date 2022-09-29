# 연결 요소의 개수 🐳
# 문제 : 연결 요소의 개수 구하기

# sys.getrecursionlimit()을 활용해 파이썬 최대 재귀 깊이 확인, 백준은 기본 1000으로 설정 🚨
sys.setrecursionlimit(10000)  # 재귀허용치를 1000 -> 10000으로 변경
input = sys.stdin.readline

N, M = map(int, input().split())

JOIN = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (N + 1)


def DFS(v):
    visited[v] = 1

    for d in JOIN[v]:
        if not visited[d]:
            DFS(d)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)
