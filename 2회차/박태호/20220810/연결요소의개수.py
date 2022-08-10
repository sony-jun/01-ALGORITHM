import sys
sys.stdin = open('연결요소의개수.txt','r')
#인접리스트 만듬

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
connect = [False]*(n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph) 

# [[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]
# [False, False, False, False, False, False, False]
# [False, True, True, True, True, True, True]
# print(connect)
start = 1
stack = [start]
connect[start] = True
cnt = 1
while stack:    
    cur = stack.pop()
    for at in graph[cur]:
        if not graph[at]:
                cnt+=1
                connect[at] = True
        else:
            if not connect[at]:
                connect[at] = True
                stack.append(at)
    if not stack and sum(connect) != n:
        cnt += 1
        for i in range(1,len(connect)):
            if connect[i] == False:
                stack.append(i)
                # print(i)
    if sum(connect) == n: break
        

print(stack, connect)
print(graph)
print(cnt)



