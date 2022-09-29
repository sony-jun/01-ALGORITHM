import sys
sys.stdin = open('지뢰찾기.txt','r')

from pprint import pprint

N = int(input()) # N x N 정사각형

mine = [list(input()) for _ in range(N)] #지뢰 메트릭스
open = [list(input()) for _ in range(N)] #열린 메트릭스

pprint(mine)
pprint(open)

mine_open = [['0']*N for _ in range(N)] # 메트릭스
pprint(mine_open)

for a in range(N):
    for b in range(N):
        if open[a][b] == '.': #아직 오픈되지 않은 곳
            mine_open[a][b] = '.'
            
pprint(mine_open)