# 촌수계산 미해결
n = int(input())
u, v = map(int, input().split())
m = int(input())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
cnt = 0
stack = [u]
result = [u]
while len(stack) != 0:
    cur = stack.pop()
    visited[cur] = True
    if cur == v:
        print(result)
        break
    for a in matrix[cur]:
        bool_list = []
        
        if visited[a] == False:
            stack.append(a)
            result.append(a)        
            cnt += 1   
        else:
            for b in matrix[cur]:
                bool_list.append(visited[b])
            if False not in bool_list:
                for _ in range(cnt):
                    result.pop()
                cnt = 0
            else:
if visited[v] == False:
    print(-1)