import sys
sys.setrecursionlimit(10000)
sys.stdin = open("20220810/11724_연결요소의개수.txt")
input = sys.stdin.readline

N, M = map(int, input().split())        # 정점 개수, 간선 개수

graph = [[] for i in range(N+1)]        # 인접 리스트
for i in range(M):                      # 간선 개수 만큼
    u, v = map(int, input().split())    # 간선 양 끝 점 u, v
    graph[u].append(v)                  # 인접 정점 추가
    graph[v].append(u)                  # 무방향이므로 반대도 추가

visited = [0] * (N+1)                   # 모든 정점 방문 확인, 초기값 0
def connect(start):                     # 시작 정점 번호 받는 함수
    visited[start] = 1                  # 방문한 정점은 1로 변경
    for i in graph[start]:              # 해당 정점과 연결된 정점
        if visited[i] == 0:             # 연결된 정점이 방문한 적 없으면
            connect(i)                  # 연결된 정점까지 순회

cnt = 0                                 # 연결 요소 개수
for i in range(1, N+1):                 # 모든 정점 1번부터 순서대로 확인
    if visited[i] == 0:                 # 해당 정점이 방문한 적 없으면
        cnt += 1                        # 새로운 연결 요소 시작이므로 개수 +1
        connect(i)                      # 연결 요소 시작
        
print(cnt)                              # 연결 요소 개수 출력