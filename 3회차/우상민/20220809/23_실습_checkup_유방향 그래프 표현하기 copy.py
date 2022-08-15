#checkup 유방향 그래프 표현하기 23
# 그래프 입력이 주어질 때 유방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.
import pprint
N, M = map(int,input().split())
matrix_ = []
answer = []
for idx in range(N+1):
    matrix_.append([0]*(N+1))
pprint.pprint(matrix_)
for i in range(M):
    a, b = map(int, (input().split()))
    matrix_[a][b] = 1
pprint.pprint(matrix_)
for index in range(N+1):
    if 1 not in matrix_[index]:
        answer.append([])
    for i_ in range(N+1):
        if matrix_[index][i_] == 1:
            answer.append([i_])
print(answer)

   


