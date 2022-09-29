import sys
sys.stdin = open("바이러스.txt")

N = int(input()) #컴퓨터 수 -
K = int(input()) #연결 수 - 간선

graph = [
    [],
    [2,5],
    [1,3,5],
    [2],
    [7],
    [1,2,6],
    [5],
    [4]
]
# for _ in range(K):
#     a, b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)

print(graph)
total = 0 #인접해있는 컴퓨터수 + 자신포함
visited = [0]*(N+1) #방문하면 1
stack = [1] #시작 위치

while len(stack) != 0: #스택에 아무것도 없으면 탈출
    cur = stack.pop() #스택 숫자를 뺴와서

    for adj in graph[cur]: #해당인덱스에 있는 값들을 넣어준다.
        if not visited[adj]: #아직 방문하지 않았으면
            visited[adj] = 1 #감염
            stack.append(adj)
            print(stack)

for bol in visited:
    if bol == 1:
        total += 1

print(visited)
print(total-1)