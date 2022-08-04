# from pprint import pprint
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    invert_matrix = []
    for row in range(m):
        mem_lst = []
        for col in range(n):
            mem_lst.append(matrix[col][row])
        invert_matrix.append(mem_lst)
    # pprint(invert_matrix)

    s = 0
    for i in range(m):
        for j in range(n):
            # pprint(invert_matrix[i][j])
            if invert_matrix[i][j] == 1:
                # pprint(f'99999 :{invert_matrix[i][j]}')
                # pprint(f'cnt :{invert_matrix[i][j+1:].count(0)}')
                s += invert_matrix[i][j+1:].count(0)
    print(s)
