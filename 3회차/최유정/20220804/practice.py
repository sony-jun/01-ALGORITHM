matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]
#mxn
#행
m = len(matrix)
#열
n = len(matrix[0])

#전치시키기
mmatrix = [[2]*n for _ in range(m)]
transposed_matrix = [[0]*m for i in range(n)]
print(mmatrix)
print(transposed_matrix)

#pythonic 이차원 리스트 총합
# total = sum(map(sum,matrix))
# print(total)

#행 우선 순회를 통한 matrix 합 구하기
# sum_ = 0
# for i in range(m):
#     for j in range(n):
#         sum_ += matrix[i][j]
# print(sum_)


#행 우선 순회
# for i in range(3):
#     for j in range(4):
#         print(matrix[i][j], end =' ')
#     print()
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2

#열 우선 순회
# 1 5 9
# 2 6 0
# 3 7 1 
# 4 8 2
# for i in range(4):
#     for j in range(3):
#         print(matrix[j][i], end =' ')
#     print()
