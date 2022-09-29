# 문제를 읽고 이해한다

# 성에 크기 즉 행렬을 만들고 모든 행과 열에 1명 이상은 경비원이 있어야한다
# 경비원에 수를 구하여라(최솟값)
# 각 행과 열에 X가 하나라도 있다면 경비원이 들어갈수가 없다!!

# 문제를 익숙한 용어로 재정의한다

# 행 N 열 M range, input
# for 반복문
# if

# 어떻게 해결할지 계획을 세운다
 
# 프로그램으로 구현한다
from pprint import pprint
matrix = []
cnt = 0
cnt1 = 0
N , M= map(int,input().split())
for i in range(N):
    array = list(input())
    matrix.append(array)
for j in range(N):
    if "X" not in matrix[j]:
        cnt += 1
for k in range(M):
    if "X" not in [matrix[j][k] for j in range(N)]:
        cnt1 += 1
print(cnt, cnt1)
# 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다