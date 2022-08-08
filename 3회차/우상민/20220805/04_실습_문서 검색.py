# 백준 문서검색 1543

matrix_ = list(map(str,(input())))
N = input()
count = 0
total = []
for i in range(len(matrix_)):
    total.append(matrix_[i])
    if N in ''.join(total):
        total.clear()
        count += 1
print(count)


