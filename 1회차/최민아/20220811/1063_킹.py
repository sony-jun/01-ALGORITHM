import sys
sys.stdin = open("20220811/1063_킹.txt")

directions = {
    'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
    'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)
}                                                       # 상하좌우, 대각선 델타

k, s, n = input().split()                               # 킹, 돌 위치, 움직이는 횟수
kx, ky = 8 - int(k[1]), ord(k[0]) - 65                  # 킹 x, y 좌표
sx, sy = 8 - int(s[1]), ord(s[0]) - 65                  # 돌 x, y 좌표

for i in range(int(n)):                                 # n번 움직임
    move = input().strip()                              # 어떻게 움직여야 하는가
    x, y = directions[move]                             # direction에서 델타 좌표 받음

    if 0 <= kx + x < 8 and 0 <= ky + y < 8:             # 킹이 이동해도 체스판 안이면
        kx += x                                         # 킹 x만큼 이동
        ky += y                                         # 킹 y만큼 이동

        if kx == sx and ky == sy:                       # 이동한 킹이 돌과 겹치면
            if 0 <= sx + x < 8 and 0 <= sy + y < 8:     # 돌을 이동해도 체스판 인이면
                sx += x                                 # 돌 x만큼 이동
                sy += y                                 # 돌 y만큼 이동
            else:                                       # 돌이 체스판을 벗어나면
                kx -= x                                 # 이동한 킹도 제자리로
                ky -= y                                 # 이동한 킹도 제자리로

    else:                                               # 킹이 체스판을 벗어나면
        continue                                        # 다음 움직임 시도

print(f'{chr(65+ky)}{str(8-kx)}')                       # 최종 킹 위치 출력
print(f'{chr(65+sy)}{str(8-sx)}')                       # 최종 돌 위치 출력