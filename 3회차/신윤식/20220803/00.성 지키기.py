# https://www.acmicpc.net/problem/1236

N, M = map(int,input().split())

# 문제에서 주어진 매트릭스 만들기
matrix = [input() for i in range(N)] 
count = 0 # 행방향으로 탐색햇을 때 인원추가해야할 때 조정해줄 숫자

for j in matrix:
    if 'X' not in j: # 만약 행방향으로 탐색했을 때 X가 없다면
        count+=1     # 인원을 배치해야함으로 count를 하나 올려줌


# 행과 열을 바꿔서 다시 매트릭스 만들기
count2 = 0  # 열방향으로 탐색햇을 때 인원추가해야할 때 조정해줄 숫자
lst2 = [] # 매트릭스 만들기

for a in range(M): 
    lst = []
    for b in range(N):
        lst.append(matrix[b][a]) # 행과 열을 뒤바꿔서 lst에 넣어줌
    lst2.append(lst) # 그 리스트를 lst2에 다시 넣어 2차원 배열을 만들어줌

# 처음 행방향 탐색과 같은 과정 반복
for k in lst2:
    if 'X' not in k:
        count2+=1

# 행 기준과 열 기준을 비교해서 더 큰 값을 출력
print(max(count,count2))