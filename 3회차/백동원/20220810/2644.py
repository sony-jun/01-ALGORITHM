# 촌수계산 
# def dfs(node):
#     for n in matrix[node]:
#         if visited[n] == 0:
#             visited[n] = visited[node]+1
#             dfs(n)
# n = int(input())
# u, v = map(int, input().split())
# m = int(input())
# matrix = [[] for _ in range(n + 1)]
# visited = [0] * (n + 1)
# for _ in range(m):
#     x, y = map(int, input().split())
#     matrix[x].append(y)
#     matrix[y].append(x)
# dfs(u)
# if visited[v] > 0:
#     print(visited[v])
# else:
#     print(-1)  

n = int(input())
u, v = map(int, input().split())
m = int(input())
matrix = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)                     # 연결되어있는 정점 사이의 거리를 나타내기 위해 false가 아닌 0으로 초기화
for _ in range(m):                          
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
stack = [u]                                 # 시작값이 들어있는 스택 선언
while len(stack) != 0:                      # 스택이 비었으면 자동으로 종료되는 while문 선언
    cur = stack.pop()                       # 스택에서 가장 나중에 추가된 값 추출하여 할당
    for a in matrix[cur]:                   # 추출된 값을 인덱스로 사용하여 인접리스트 순회
        if visited[a] == 0:                 # 만약 방문된 적이 없는 값이라면, 
            visited[a] = visited[cur] + 1   # + 1 된 값을 대입한다.
            stack.append(a)                 # 스택에 추가.  결국 시작값에서 한칸씩 멀어질수록 1씩 증가한 값이 visited 리스트에 할당됨
if visited[v] > 0:                          # 찾고자하는 값이 방문된 적이 있다면
    print(visited[v])                       # 그 거리가 기록된 visited 리스트를 인덱스를 활용하여 출력
else:
    print(-1)                               # 방문된 적이 없다면 -1 출력(연결되어있지 않다는 뜻)