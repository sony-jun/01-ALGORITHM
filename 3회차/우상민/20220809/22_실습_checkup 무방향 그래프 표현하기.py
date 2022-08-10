#checkup 무방향 그래프 표현하기 22
# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

import pprint
N, M = map(int,input().split())
matrix_ = []

for idx in range(M+2):
    matrix_.append([0]*(N+2))
for i in range(1, N):
    u, v = map(int,input().split())    
    matrix_[u][v] = 1
    matrix_[v][u] = 1
record = []
for index in range(M+2):
    record_1 = []
    if 1 not in matrix_[index] :
            record_1.append([''])
    record.append(record_1)
    record_1.clear()
    for i_ in range(M+2):
        if matrix_[index][i_] == 1:
            record_1 += [i_]
pprint.pprint(matrix_)
pprint.pprint(record)


