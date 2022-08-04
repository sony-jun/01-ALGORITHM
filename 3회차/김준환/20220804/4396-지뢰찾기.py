# 함수로 주변 지뢰 개수 탐색 구현 필요할때만 돌아서 효율 향상
# import sys
# input = sys.stdin.readline

from pprint import pprint

size = int(input())

ziroe_matrix = [['.'] + list(input()) + ['.'] for _ in range(size)]
ziroe_matrix.insert(0,['.']*(size+2))
ziroe_matrix.append(['.']*(size+2))
# pprint(ziroe_matrix)
open_matrix = [list(input()) for _ in range(size)]
# pprint(open_matrix)
success_matrix = [['.']*size for _ in range(size)]
fail_matrix = [['.']*size for _ in range(size)]

def Ziroe_Count(col,row):
    i = col + 1
    j = row + 1
    cnt = 0
    for idx_i in range(i-1,i+2):
        for idx_j in range(j-1,j+2):
            if ziroe_matrix[idx_i][idx_j] == '*':
                cnt += 1
    return cnt

game_over = False
for col in range(size):
    for row in range(size):
        if open_matrix[col][row] == 'x':
            if ziroe_matrix[col+1][row+1] == '*':
                fail_matrix[col][row] = '*'
                game_over = True
            else:
                number = Ziroe_Count(col,row)
                success_matrix[col][row] = number
                fail_matrix[col][row] = number
        else:
            if ziroe_matrix[col+1][row+1] == '*':
                fail_matrix[col][row] = '*'

if game_over == True:
    for col in range(size):
        for row in fail_matrix[col]:
            print(row,end='')
        print()
else:
    for col in range(size):
        for row in success_matrix[col]:
            print(row,end='')
        print()

# pprint(fail_matrix)
# pprint(success_matrix)