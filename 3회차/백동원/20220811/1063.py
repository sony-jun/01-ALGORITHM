import sys
sys.stdin = open('1063.txt')

movement = {
    'R'     : (0, 1),                                        # 움직임을 나타내는 딕셔너리 작성
    'L'     : (0, -1),
    'B'     : (-1, 0),
    'T'     : (1, 0),
    'RT'    : (1, 1),
    'LT'    : (1, -1),
    'RB'    : (-1, 1),
    'LB'    : (-1, -1)
}
K, S, N = input().split()
kx = ord(K[0]) - 65           # 입력값을 통해 8행 8열의 체스판에서 위치를 할당
ky = int(K[1]) - 1
sx = ord(S[0]) - 65
sy = int(S[1]) - 1
for _ in range(int(N)):
    moving = input()
    mx = movement.get(moving)[1]    # 입력값을 통해 딕셔너리에서 이동방향을 추출하여 할당
    my = movement.get(moving)[0]    
    if (0 <= kx + mx <= 7) and (0 <= ky + my <= 7):         # 킹이 이동 후에 체스판을 벗어나지 않고,
        if (kx + mx != sx) or (ky + my != sy):              # 돌과 좌표가 겹치지 않는다면,
            kx += mx                                        # 이동 후 좌표가 킹의 좌표로 확정
            ky += my
        elif (kx + mx == sx) and (ky + my == sy):           # 만약 돌과 좌표가 겹치고,
            if (0 <= sx + mx <= 7) and (0 <= sy + my <= 7): # 돌이 이동 후에 체스판을 벗어나지 않는다면,
                kx += mx                                    # 돌과 킹 둘다 이동
                ky += my
                sx += mx
                sy += my
print(chr(kx + 65) + str(ky + 1))                           # 기존 좌표방식으로 원복하여 출력
print(chr(sx + 65) + str(sy + 1))