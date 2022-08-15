# 백준 직사각형 네개의 합집합의 면적 구하기
matrix_ = []

for i in range(4):
    x_1, y_1, x_2, y_2 = map(int,(input().split()))
    for idx in range(x_1, x_2):
        for index in range(y_1, y_2):
            matrix_.append([idx,index])
print(matrix_)

print((set(map(tuple, matrix_))))