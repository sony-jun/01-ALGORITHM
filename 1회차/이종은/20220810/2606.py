# 바이러스
import sys 
sys.stdin = open('input.txt')

n = int(input()) # 정점 개수(컴퓨터)
m = int(input()) # 간선 개수(네트워크)

# n = 7 1번부터 7번까지

graph = []
for _ in range(n+1): # n+1인 이유는? 0부터 시작한다고 하지만, 실제는 1번부터이기 때문 7인덱스와 컴퓨터 번호 7과 맞추어야함
    graph.append([])

# graph = [[]for _ in range(n+1)]

visited = [False]*(n+1) # 방문 처리 리스트 만들기 
# total = 0

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


stack = [1] # 처음 시작 숫자이며, 돌아갈 곳을 기록하기 위해 스택에 넣어줌
visited[1] = True # 시작 정점 방문 기록 

cnt = 0

while stack: #스택이 빌 때까지, 돌아갈 곳이 없을때까지 반복
    cur = stack.pop() # 현재 방문 정점(후입선출: 최근에 들어온 것 부터 먼저 나감)
    
    for i in graph[cur]: # 인접한 모든 정점에 대해
        if not visited[i] : # 아직 방문하지 않았다면
                visited[i] = True # 방문 처리 
                stack.append(i) # 스택에 넣기


for j in range(len(visited)):
    if visited[j] == True: 
        cnt += 1

print(cnt-1)

        

# 1번과 연결 된 정점 갯수 세기, 스택에 몇번이나 값을 넣느냐





