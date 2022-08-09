from re import L
import sys
from pprint import pprint
sys.stdin = open('4.txt','r')

omok = [list(map(int,input().split())) for _ in range(19)]
b_cnt = 0
w_cnt = 0

b_win = []
w_win = []

del_x = [-1,0,1,1]
del_y = [1,1,1,0]

for x in range(19):
    for y in range(19):

        # 바둑판에서 0이 아니면 돌임
        if omok[x][y] != 0:
            dol = omok[x][y]

        for k in range(4):
            cnt = 1
            ox = x + del_x[k]
            oy = y + del_y[k]
            if 0 <= ox < 19 and 0 <= oy < 19 and omok[ox][oy] == dol:
                cnt += 1
                
                if cnt == 5:
                    if 0 <=