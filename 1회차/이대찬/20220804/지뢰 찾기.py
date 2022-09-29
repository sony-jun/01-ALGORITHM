import sys

sys.stdin = open('지뢰 찾기.txt')

N = int(input())

matrix_1 = [list(input()) for _ in range(N)]
matrix_2 = [list(input()) for _ in range(N)]

try:
    for R in range(N):
        for C in range(N):
            if matrix_2[R][C] == 'x':
                cnt = 0
                try:
                    for r in range(3):
                        for c in range(3):
                            if R-1+r < 0  or C-1+c < 0:
                                continue
                            if matrix_1[R-1+r][C-1+c] == '*':
                                cnt += 1
                except:
                    pass
                matrix_2[R][C] = cnt
            print(matrix_2[R][C],end='')
        print()
except:
    pass
