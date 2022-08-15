#checkup 유방향 그래프 표현하기 23
# 그래프 입력이 주어질 때 유방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.
import pprint
N, M = map(int,input().split())
matrix_ = []
for i in range(N):
    matrix_.append(list(str(input())))
Car_0 = 0
Car_1 = 0
Car_2 = 0
Car_3 = 0
Car_4 = 0
for idx in range(N-1):
    for index in range(M-1):
        count = 0
        if matrix_[idx][index] != '#' and matrix_[idx][index+1] != '#' and matrix_[idx+1][index] != '#' and matrix_[idx+1][index+1] != '#':
            if matrix_[idx][index] == 'X':
                count += 1
            if matrix_[idx][index+1] == 'X':
                count += 1
            if matrix_[idx+1][index] == 'X':
                count += 1
            if matrix_[idx+1][index+1] == 'X':
                count += 1
        else:
            count += 10
        if count == 0:
            Car_0 += 1
        elif count == 1:
            Car_1 += 1
        elif count == 2:
            Car_2 += 1
        elif count == 3:
            Car_3 += 1
        elif count == 4:
            Car_4 += 1        
print(Car_0)
print(Car_1)
print(Car_2)
print(Car_3)
print(Car_4)

