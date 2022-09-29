# 바이러스에 걸린 1번 컴퓨터와 연결된 컴퓨터들만 추적합니다.
# 인풋 받기
# 빈 인접리스트 생성
# 인접 리스트 append
# 방문기록 생성
# dfs 함수 선언
# 함수 실행
# 결과값 출력

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit=[0]*(n+1)

def dfs(graph, v, visited):
    visit[v] = 1 
    for i in graph[v]: 
        if visit[i] == 0 : 
            dfs(graph, i, visited)

dfs(graph, 1, visit)
print(visit.count(1)-1)