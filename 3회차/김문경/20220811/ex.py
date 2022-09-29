import sys
from pprint import pprint
sys.stdin = open('test.txt')

# 기본 체스판
chess = [['0'] * 8 for i in range(8)]

# 가로 세로 좌표 위한 리스트
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rows = ['8', '7', '6', '5', '4', '3', '2', '1']

# 상 부터 시계방향으로 8방향
# 만약 입력이 RB로 들어온다면 딕셔너리를 통해 (1,1)의 델타에 접근가능
directions = {'T' : (-1, 0), 
              'RT' : (-1, 1), 
              'R' : (0, 1), 
              'RB' : (1, 1), 
              'B' : (1, 0), 
              'LB' : (1, -1), 
              'L' : (0, -1), 
              'LT' : (-1, -1)
}
# x = 'A2'
# print(list(''.join(x))) # ['A', '2'] 로 나눌 수 있음

# 입력 받기
king = 'B3'
stone = 'C5'

# 일단 위치 먼저 (그 후 반복에서도 항상 위치 업데이트)
#* 킹
king_now = list(''.join(king))
ky = columns.index(king_now[0]) # A2가 현재위치일때 king_now[0]이 'A', A의 인덱스를 변수에 저장
kx = rows.index(king_now[1])
chess[kx][ky] = '#'
#* 돌
stone_now = list(''.join(stone))
sy = columns.index(stone_now[0]) 
sx = rows.index(stone_now[1])
chess[sx][sy] = '@'

cmd = directions['B']

new_ky = ky + cmd[1]
new_kx = kx + cmd[0]
chess[kx][ky] = '0'
chess[new_kx][new_ky] = '#'
print(new_ky, new_kx)
pprint(chess)