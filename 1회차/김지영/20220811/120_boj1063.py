# 8*8의 board
# 알파벳 = 열, A → H
# 숫자 행 8 ↓ 1
import sys
sys.stdin = open('120_input.txt')
def ppr(lst):
    for i in lst:
        print(i)
delta = {'R' : (0,1), # (y,x) 변화량
        'L' : (0,-1),
        'B' : (1,0),
        'T' : (-1,0),
        'RT' : (-1,1),
        'LT' : (-1,-1),
        'RB' : (1,1),
        'LB' : (1,-1)}
# stone은 king이 움직인 방향과 같은 방향으로 1칸 이동
# if king or stone out of range = skip
alpha = { 'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
        'F' : 5,
        'G' : 6,
        'H' : 7}
k,s,n = input().split() # input A1 A2 5
kx,ky = alpha[k[0]],8-int(k[1]) # 0,7
sx,sy = alpha[s[0]],8-int(s[1]) # 0,6
board = ['.'* 8 for _ in range(8)]

move = []
for _ in range(int(n)):
    move = input()

    king = board[ky][kx]
    stone = board[sy][sx]

    nky = ky + delta[move][0]
    nkx = kx + delta[move][1]
    nsy = sy + delta[move][0]
    nsx = sx + delta[move][1]
    # print(kx,ky,sx,sy)
    # 킹 이동좌표 = 돌 좌표, 돌 좌표 + 킹 변화량 and 킹좌표 != 돌좌표
    if (nky,nkx) == (sy,sx) and 0<= nsy < 8 and 0<= nsx < 8:
        # print('stone_move',move,nkx,nky,nsx,nsy)
        sy = nsy
        sx = nsx
    # 돌 이동 후, 킹의 위치 변화
    if (sy,sx) != (nky,nkx) and 0<= nky < 8 and 0 <= nkx < 8 :
        # print(move,nkx,nky,nsx,nsy)
        ky = nky
        kx = nkx

# 인덱스 변환 원상복구~
def get_key(value):
    for k,v in alpha.items():
        if v == value:
            return k
kx = get_key(kx) # type(str)
ky = 8 - ky # type(int)
sx = get_key(sx)
sy = 8 - sy
king = kx + str(ky)
stone = sx + str(sy)
print(king)
print(stone)
