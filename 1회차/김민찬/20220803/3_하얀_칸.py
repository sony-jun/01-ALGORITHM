import sys

sys.stdin = open("3_하얀_칸.txt")

Matrix = []
for _ in range(8): # 8 X 8
    Matrix.append(list(map(str, list(input()))))

# 하 검 하 검 하 검 하 검 0 2 4 6
# 검 하 검 하 검 하 검 하 2 4 6 8
# 하 검 하 검 하 검 하 검 0 2 4 6
# 검 하 검 하 검 하 검 하 2 4 6 8
# 하 검 하 검 하 검 하 검 0 2 4 6
# 검 하 검 하 검 하 검 하 2 4 6 8
# 하 검 하 검 하 검 하 검 0 2 4 6
# 검 하 검 하 검 하 검 하 2 4 6 8

chess = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: # 하얀 칸일 경우 -> 행 + 열 = 짝수
            if Matrix[i][j] == 'F': # F가 있을 경우
                chess += 1
print(chess)