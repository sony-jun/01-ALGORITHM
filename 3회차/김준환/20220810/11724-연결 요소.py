# m, n = map(int,input().split())
# a, b = map(int,input().split())
# lst = [{a,b}]
# for _ in range(n-1):
#     n1, n2 = map(int,input().split())
#     for group in lst:
#         if n1 in group or n2 in group:
#             if n1 in group:
#                 group.add(n2)
#             if n2 in group:
#                 group.add(n1)
#             break
#     else:
#         lst.append({n1,n2})
#     print(lst)
# print(len(lst))


# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())         # 정점 개수, 관계 개수
# input_lst = []           
# for _ in range(m):
#     input_lst.append(list(map(int,input().split())))
# print(input_lst)
# group_lst = [{*input_lst[0]}]
# cnt = 0
# while cnt < m+1:
#     print(group_lst)
#     cnt += 1
#     for case in input_lst:
#         for group_set in group_lst:
#             if case[0] in group_lst or case[1] in group_set:
#                 if case[0] in group_set:
#                     group_set.add(case[1])
#                 if case[1] in group_set:
#                     group_set.add(case[0])
#                 break
#         group_lst.append({case[0],case[1]})
# print(group_lst)
# print(len(group_lst)-1)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    cnt = 0
    # stack = [start]
    visited[start] = True
    # for i in range(len(visited)):
    #     if visited[i] == False:
    #         if cnt == 0:
    #             pass
    #         else:
    #             stack = [i]
    visited[0] = True
    while True:
        visit = 0
        for i in range(n+1):
            if visited[i] == False:
                stack = [i]
            else:
                visit += 1
        if visit == n+1:
            return cnt
        while stack:
            # print(f'v : {visited}')
            # print(f'stack : {stack}')
            # print(f'graph : {graph}')
            cur = stack.pop()

            for adj in graph[cur]:
                if visited[adj] == False:
                    visited[adj] = True
                    stack.append(adj)

            #  print(visited)
        cnt += 1
    return cnt
print(dfs(1))