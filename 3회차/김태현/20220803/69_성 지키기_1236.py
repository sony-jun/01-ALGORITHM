import sys
sys.stdin = open("69_성 지키기_1236.txt", "r")

# 반복문으로 각 줄을 리스트로 입력 받음
# 각 줄에 X 위치 값을 모두 저장
# X의 위치 값 리스트가, x축: i ~ N, y축: 1 ~ N을 모두 커버하는지 확인

N, M = map(int, input().split())

matrix = [] # [['....'], ['....'], ['....'], ['....']]
for i in range(N):
    matrix.append(list(input().split()))

# for i in range(N):
#     matrix.append(input())
print(matrix, "matrix")

set_X = set()
set_Y = set()

for j in range(len(matrix)): # mat = ['XX...']의 형태이므로
    line = matrix[j][0] # matrix[j] = ['XX...'], matrix[j]0] = 'XX...'
    
    for k in range(len(line)):
        if "X" == line[k]:
            # print(j, k)
            set_X.add(j) # 행
            set_Y.add(k) # 열
    
# print(set_X, "set_X")
# print(set_Y, "set_Y")

result = [N - len(set_X), M - len(set_Y)] # 최소 채워야 하는 행 개수, 열 개수

if max(result): # 주어진 행 * 렬 값과 차이가 큰 경우 = 최소 채워야 하는 X 수
    print(max(result))
else:
    print(0)