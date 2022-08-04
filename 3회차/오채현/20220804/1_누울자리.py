# 행과 열 마다 각각 2개 연속칸이 비어있으면 ok
n = 5

# matrix = [list(input()) for _ in range(n)]

matrix = [
    ['.', '.', '.', '.', 'X'],
    ['.', '.', 'X', 'X', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', 'X', 'X', '.', '.'],
    ['X', '.', '.', '.', '.']
]

bplaceR = 0
bplaceC = 0

for i in range(n):
    cntrow = 0
    cntcol = 0
    for j in range(n):
        # 행 순회
        if matrix[i][j] == '.':
            cntrow += 1
        else:
            cntrow = 0
        if cntrow == 2:
            bplaceR += 1

        # 열 순회
        if matrix[j][i] == '.':
            cntcol += 1
        else:
            cntcol = 0
        if cntcol == 2:
            bplaceC += 1

print(bplaceR, bplaceC)
