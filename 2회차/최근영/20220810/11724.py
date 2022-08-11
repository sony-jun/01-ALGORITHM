from pprint import pprint
n,m = list(map(int,input().split()))
matrix = [[] for __ in range(n+1)]

for i in range(m):
    x, y = map(int,input().split())
    matrix[x].append(y)
    matrix[y].append(x)
total_list=[]
pprint(matrix)
for j in range(1,len(matrix)):
    stack = list(matrix[j])
    visit = [False]*(n+1)
    visit[j] = True
    while stack:
        cur = stack.pop()
        for k in matrix[cur]:
            if visit[k] == False:
                visit[k] = True
                stack.append(k)
    print(visit)