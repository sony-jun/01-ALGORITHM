# https://www.notion.so/hphk-edu/22-edea5d6c9e9946c1924dbee716cb9df7
import sys
sys.stdin = open('Q22.txt')

V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]
adj_list = [[] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = map(int, input().split())
    
    adj_matrix[v1][v2] = 1 
    
    adj_list[v1].append(v2)
    
print(adj_matrix)
print(adj_list)
