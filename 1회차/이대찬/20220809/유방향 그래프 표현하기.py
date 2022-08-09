import sys

sys.stdin = open('무방향 그래프 표현하기.txt')

n,m = map(int,input().split())
result_matrix = [[0]*(n+1) for _ in range(n+1)]

result_list = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    result_list[u].append(v)
    
    result_matrix[u][v] = 1
    
print(result_matrix)    
print(result_list)

    
    
 
 