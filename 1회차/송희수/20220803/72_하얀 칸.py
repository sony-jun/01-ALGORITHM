import sys

sys.stdin = open("72_하얀 칸.txt")

m = 8
n = 8

matrix = [list(map(str, input())) for tc in range(n)]
result = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if matrix[i][j] == 'F':
                result +=1
print(result)