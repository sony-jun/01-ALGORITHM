n = int(input())
start, end = list(map(int, input().split()))

m = int(input())

graph = [[] for _ in range(0, n + 1)]

for _ in range(m):

    x, y = list(map(int, input().split()))

    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

stack = []
stack.append((start, 0))
visited[start] = True

# 장답을 출력할 변수
answer = -1

# 스택이 비어있지 않으면 반복
while len(stack) != 0:
    number, count = stack.pop()

    if number == end:
        answer = count
        break

    adj_graph = graph[number]

    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        if not visited[adj_number]:
            stack.append((adj_number, count + 1))
            visited[adj_number] = True

# 촌수 출력
print(answer)
