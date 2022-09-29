# https://www.notion.so/hphk-edu/21-bb38e88c331a46628d5c6ee33ddcd50c
import sys
sys.stdin = open('Q21.txt')

V, E = map(int, input().split())
adj_matrix = [[0] * (V+1) for _ in range(V+1)]
adj_list = [[] * (V+1) for _ in range(V+1)]
# print(adj_matrix, adj_list)

for i in range(E):
    v1, v2 = map(int, input().split())
    # print(v1, v2)
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1
    
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
    
print(adj_matrix)
print(adj_list)

    
    

