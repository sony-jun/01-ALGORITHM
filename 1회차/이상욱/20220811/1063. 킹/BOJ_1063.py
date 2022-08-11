from pprint import pprint
import sys
sys.stdin = open('1063.txt')
dict = {                                           # 킹이 움직일 수 있는 좌표 
    'R' : (0, 1), 'L' : (0, -1), 
    'B' : (1, 0), 'T' : (-1, 0),
    'RT' : (-1, 1), 'LT' : (-1, -1), 
    'RB' : (1, 1), 'LB' : (1, -1)}

# for _ in range(8):                                 # 체스판 8*8
#     li = [[0] * 8 for i in range(8)]

king, stone, N = input().split()                   # 킹위치, 스톤위치, 움직인 횟수
                                                   #   A1      A2           1  
kx, ky = 8 - int(king[1]), ord(king[0])-65         # kx = 7, ky = 0   
sx, sy = 8 - int(stone[1]), ord(stone[0])-65       # sx = 6, sy = 0

for i in range(int(N)):
    move = input()                                 # T (-1, 0)
    nkx = kx + dict[move][0]                       # 7+(-1) = 6
    nky = ky + dict[move][1]                       # 0+0 = 0
   
    if 0 <= nkx < 8 and 0 <= nky < 8:
        if nkx == sx and nky == sy:                # T (-1, 0)
            nsx = sx + dict[move][0]               # 6+(-1) = 5
            nsy = sy + dict[move][1]               # 0+0 = 0

            if 0 <= nsx < 8 and 0 <= nsy < 8:
                kx, ky = nkx, nky
                sx, sy = nsx, nsy
        else:
           kx, ky = nkx, nky 

ky, kx = chr(ky+65), 8 - kx
sx, sy = 8 - sx, chr(sy+65)
print(f'{ky}{kx}')
print(f'{sy}{sx}')