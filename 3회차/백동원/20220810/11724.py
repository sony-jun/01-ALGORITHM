# 연결 요소의 개수
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)
cnt = 0
for a in range(1, N + 1):
    stack = [a]
    if visited[a] == False:
        while len(stack) != 0:
            cur = stack.pop()
            visited[cur] = True
            for i in matrix[cur]:
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)
        cnt += 1
print(cnt)

# N, M = map(int, input().split())
# matrix = [[] for _ in range(N + 1)]
# result_list = []
# for _ in range(M):
#     u, v = map(int, input().split())
#     matrix[u].append(v)
#     matrix[v].append(u)
# for a in range(1, N + 1):
#     result = []
#     visited = [False] * (N + 1)
#     stack = [a]
#     while len(stack) != 0:
#         cur = stack.pop()
#         visited[cur] = True
#         for i in matrix[cur]:
#             if visited[i] == False:
#                 visited[i] = True
#                 stack.append(i)
#     for j in range(1, N + 1):
#         if visited[j] == True:
#             result.append(j)
#     result.sort()
#     if result not in result_list:
#         result_list.append(result)
# print(len(result_list))