import sys
sys.stdin = open("70_유니크_5533.txt", "r")

# 첫번째 사람을 최초값으로 저장
# 동일하면 += 0

N = int(input())

# 행 * 렬 -> 열 * 행 바꾸기
matrix = [[], [], []]
sum = []

# 구글링: 행 * 열 -> 열 * 행
for _ in range(N):
    a, b, c = map(int, input().split())
    matrix[0].append(a)
    matrix[1].append(b)
    matrix[2].append(c)

for i in range(N): # 플레이어 5
    score = 0
    for j in range(3): # 게임 3
        if matrix[j].count(matrix[j][i]) == 1:
            score += matrix[j][i]
    sum.append(score)

for i in sum:
    print(i)


# [1, 1] [1, 2] [1, 3]
# [2, 1] [2, 2] [2, 3]