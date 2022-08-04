N = int(input())
numbers = []

# matrix N X 3 행렬
for _ in range(N):
    numbers.append(list(map(int, input().split())))

# 열 숫자를 비교했을 때 같은 점수 있으면 점수 못가져감
# 같은 점수가 없을 경우 점수 가져감

for j in range(3):
    for i in range(N):
        if numbers[i][j] == numbers[i][j]:
            if i != i:
