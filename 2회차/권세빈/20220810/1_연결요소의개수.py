import sys
sys.stdin = open('1.txt', 'r')
input = sys.stdin.readline

n, m = map(int,input().split()) # 정점 개수, 간선 개수

 # 인접리스트 생성
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 처리용
v = [False] * (n + 1)
# 연결요소 개수
cnt = 0

# dfs 함수
def dfs(start):
    stack = [start]
    v[start] = True
    while stack:
        cur = stack.pop()
        for j in graph[cur]:
            if not v[j]:
                v[j] = True
                stack.append(j)

# 1 ~ n까지의 정점 방문 확인
for k in range(1,n+1):
    
    # False라면 dfs 함수 적용해서 True로 바꾸기
    if v[k] == False:
        dfs(k)
        # dfs 함수 끝나면 카운트 1씩 해주기
        cnt += 1
    
print(cnt)

