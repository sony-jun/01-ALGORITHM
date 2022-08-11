import sys
sys.stdin = open('1063.txt')
# 8방향 델타값 이용
directions = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}
# 'A' -> 65, 문자를 아스키코드로 변경
k, s, n = input().split()
kx = 8 - int(k[1])
ky = ord(k[0]) - 65
sx = 8 - int(s[1])
sy = ord(s[0]) - 65
# 킹과 돌의 위치 입력받은대로 움직이기
for _ in range(int(n)):
    how_move = input()
    go_x, go_y = directions[how_move]
    
    if not (0 <= kx + go_x < 8 and 0 <= ky + go_y < 8):
        continue
    kx += go_x
    ky += go_y

    if (kx, ky) == (sx, sy):
        # 돌이 밖으로 나가면
        if not (0 <= sx + go_x < 8 and 0 <= sy + go_y < 8):
            # 킹의 움직임 되돌리기
            kx -= go_x
            ky -= go_y
            continue
        sx += go_x
        sy += go_y

result_k = chr(ord('A') + ky) + str(8 - kx)
print(result_k)
result_s = chr(ord('A') + sy) + str(8 - sx)
print(result_s)
