# 백준 박스 9455



for S in range(int(input())):
    matrix_ = []
    count = 0
    H, W = map(int, input().split())
    for s in range(H):
        matrix_.append(list(input().split()))
    for i in range(1, H):
        for idx in range(W):
            if matrix_[i-1][idx] == str(1) and matrix_[i][idx] != str(1):
                matrix_[i-1][idx] = str(0)
                matrix_[i][idx] = str(1)
                count += 1
    print(count)

            