from pprint import pprint 

n,m = map(int,(input().split()))

graph = [[0]*(n+1) for _ in range(n+1)] #리스트 만들기
matrix = [[] for _ in range(n+1)]

for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

    matrix[v1].append(v2)
    matrix[v2].append(v1)

pprint(graph)
pprint(matrix)


