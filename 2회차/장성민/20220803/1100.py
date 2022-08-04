from pprint import pprint

matrix = []

# 입력되는 값들 리스트로 구성
for _ in range(8):
    line = list(input())
    matrix.append(line)

# 흰색 위에 말 개수
result = 0
# i+j의 값이 짝수일 경우 흰색이기 때문에 'F' 확인
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if matrix[i][j] == 'F':
                result += 1

print(result)

