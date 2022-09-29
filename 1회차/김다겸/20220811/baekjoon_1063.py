import sys
sys.stdin = open("input.txt")

directions = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (1, 0),
    'T' : (-1, 0),
    'RT' : (-1, 1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (1, -1)
}

k, s, n = input().split()

# 킹과 돌의 위치
kx, ky = 8 - int(k[1]), ord(k[0]) - 65
sx, sy = 8 - int(s[1]), ord(s[0]) - 65

for i in range(int(n)):
    dir = input()
    for j in range(8):
        # 8방위 탐색
        nkx = kx + directions[dir][0]
        nky = ky + directions[dir][1]
        # 킹이 옮기는 자리에 돌이 있으면
        if nkx == sx and nky == sy:
            # 킹의 자리 = 돌의 자리 + 그 방향에 1 더하기
            nsx = sx + directions[dir][0]
            nsy = sy + directions[dir][1]
        # 킹이 옮기는 자리에 돌이 없으면
        else:
            # 돌은 가만히
            nsx = sx
            nsy = sy
    # 킹과 돌이 판을 나가지 않으면
    if 0 <= nkx < 8 and 0 <= nky < 8 and 0 <= nsx < 8 and 0 <= nsy < 8:
        # 현재 돌을 옮긴 돌로 바꾸기
        kx = nkx
        ky = nky
        sx = nsx
        sy = nsy

# 답을 출력 형식으로 바꾸기
ans_k = chr(ky+65) + str(8 - kx)
ans_s = chr(sy+65) + str(8 - sx)
print(ans_k)
print(ans_s)