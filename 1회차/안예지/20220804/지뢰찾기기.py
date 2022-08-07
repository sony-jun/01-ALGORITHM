# 4396.

"""
1. 주어진 지뢰 격자 배열을 순회하면서
2. 플레이어가 오픈한 칸의 상하좌우 대각선으로 지뢰가 있는 지 확인하고
3. 있으면 지뢰 수를 결과 칸에 표시한다.
4. 상하좌우 대각선 탐색할 칸은 지뢰 격자의 범위를 넘지 않는다.
5. 만일 오픈된 칸이 지뢰라면, 해당 격자의 지뢰가 있는 모든 칸이 *표시되어야 한다.
6. 이를 결과 격자에 출력한다.
7. 결과 격자는 지뢰 격자와 동일한 크기를 가진다.

"""
from pprint import pprint

n = 8
# n = int(input())
star_matrix = [
    '...**..*',
    '......*.',
    '....*...',
    '........',
    '........',
    '.....*..',
    '...**.*.',
    '.....*..'
 ]
# star_matrix = list(input() for _ in range(n))
open_matrix = [
    'xxx.....',
    'xxxx....',
    'xxxx....',
    'xxxxx...',
    'xxxxx...',
    'xxxxx...',
    'xxx.....',
    'xxxxx...'
    ]
# open_matrix = list(input() for _ in range(n))
result = list(['.'] * n for _ in range(n))
# result = []
# for _ in range(n):
#     temp = ['.'] * n
#     result.append(temp)

dr = [0, 0, -1, -1, -1, 1, 1, 1]
dc = [0, 0, -1, -1, -1, 1, 1, 1]
star_matrix = list(star_matrix)
open_matrix = list(open_matrix)

for r in range(len(star_matrix)):
    for c in range(len(star_matrix[0])):
        cnt_star = 0
        if open_matrix[r][c] == 'x':
        
            for d in range(8):
                dr_r = r + dr[d]
                dc_c = c + dc[d]
                if 0 <= dr_r <= n -1 and 0 <= dc_c <= n - 1: 
                    if star_matrix[dr_r][dc_c] == '*':
                        print(dr_r, dc_c)
    
    print("-----")       
#                         cnt_star += 1
                        
#             result[r][c] = cnt_star
# pprint(result)