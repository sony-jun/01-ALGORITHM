import sys

sys.stdin = open("0_성_지키기.txt")

N, M = map(int,input().split()) # N -> 행, M -> 열
Matrix = [] # Matrix 라는 리스트 생성
for _ in range(N):
    Matrix.append(input())

A = 0
B = 0
for i in range(N):
    if 'X' not in Matrix[i]: # 행마다 X가 들어있지 않은 개수 구하기
        A += 1

for j in range(M):
    # if 'X' not in Matrix[j]: # 예제 1 빼고는 모두 에러 # IndexError: list index out of range
    if 'X' not in [Matrix[i][j] for i in range(N)]: # 열마다 X가 들어있지 않은 개수 구하기
        B += 1

# print(min(A, B))
print(max(A, B)) # 그 중 큰 값을 출력