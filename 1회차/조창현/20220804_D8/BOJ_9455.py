from pprint import pprint
import sys

sys.stdin = open('9455.txt')

T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    tet = [list(map(int, input().split())) for i in range(m)]
    #print(tet)

    trans_tet = [[0] * m for i in range(n)]
    #pprint(trans_tet)
    for r in range(m):
        for c in range(n):
            trans_tet[c][r] = tet[r][c]
    #pprint(trans_tet)

    mov_cnt = 0
    for r in range(n):
        for c in range(m):
            if trans_tet[r][c] == 1:
                #print('1')
                for i in range(c, m):
                    if trans_tet[r][i] == 0:
                        mov_cnt += 1
    print(mov_cnt)