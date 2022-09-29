n, m = 2, 3
# matrix = [list(map(int, input()))]
matrix = [
    [1, 2, 4],
    [8, 16, 32]
]

# for _ in range(k):
    # i, j, x, y = map(int, input().split())

    # i, j, x, y = 1, 1, 2, 3

k = 3
i, j, x, y = 1, 1, 2, 3 #matrix(1,1) 부터 matrix(2, 3)까지의 합 = 행렬 전체의 합
#i, x = > 행  // j, y => 열 ==== 인덱스로 접근하려면 -1 해줘야 함
# print(matrix[i-1][j-1], matrix[x-1][y-1])
#행 중에 최대 값 찾아서 새로운 행 값에 대입, 열 중에 최대 값 찾아서 새로운 열 값에 대입

total = 0

for row in range(i - 1, x):
    for col in range(j - 1, y):
        total += matrix[row][col]
print(total)

#-------

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())
    total = 0

    for row in range(i - 1, x):
        for col in range(j - 1, y):
            total += matrix[row][col]

    print(total)
