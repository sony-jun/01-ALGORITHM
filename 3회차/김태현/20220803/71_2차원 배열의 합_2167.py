import sys
sys.stdin = open("71_2차원 배열의 합_2167.txt", "r")

N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

K = int(input())

for k in range(K): # 3번 반복
    i, j, x, y = map(int, input().split())

    sum = 0
    for a in range(min(i, x)-1, max(i, x)):
        for b in range(min(j, y)-1, max(j, y)):
            sum += matrix[a][b]
    print(sum)

# [1, 1] [1, 2] [1, 3]
# [2, 1] [2, 2] [2, 3]

# [1, 2,  4]
# [8, 16, 32]