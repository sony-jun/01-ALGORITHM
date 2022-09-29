from pprint import pprint

n = 5 # 행의 개수
m = 10 # 열의 개수

matrix = [[0] * m for _ in range(n)]

pprint(matrix)


# # 리스트 컴프리 헨션을 통해 이차원 리스트의 입력을 간단히 받을 수 있다
# matrix = [list(input()) for _ in range(8)]

# for i in matrix:
#     print(i)

# # 행렬의 크기가 미리 주어지는 경우

# matrix = []

# for _in range(8):
#     line = list(input())
#     matrix.append(line)