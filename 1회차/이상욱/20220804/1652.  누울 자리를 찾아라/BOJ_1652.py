import sys
sys.stdin = open('1652.txt')

N = int(input())                # 맨 첫줄 길이를 받고,
condo = [list(input()) for _ in range(N)]

Xcnt = 0 # 가로 누울자리 수
for i in range(N):
    blank_X = 0
    for j in range(N):
        if condo[i][j] == '.':      # 리스트를 돌면서 .이 있으면 빈칸 +1
            blank_X += 1
        elif condo[i][j] == 'X':    # 리스트를 돌다가 X를 만나면
            if blank_X >= 2:        # X가 2 이상인경우
                Xcnt += 1           # 가로 누울자리 +1
                blank_X = 0         # 빈칸 초기화
            else:                   # X가 2보다 작은 경우
                blank_X = 0         # 누울자리 추가 안하고 초기화
    if blank_X >= 2:                # 리스트에 X를 만나지 않고 끝났을 경우
        Xcnt += 1                   # 빈칸 2 이상이면 가로 누울자리 하나 추가

Ycnt = 0 # 세로 누울자리 수
for i in range(N):
    blank_Y = 0
    for j in range(N):
        if condo[j][i] == '.':
            blank_Y += 1
        elif condo[j][i] == 'X':
            if blank_Y >= 2:
                Ycnt += 1
                blank_Y = 0
            else:
                blank_Y = 0
    if blank_Y >= 2:
        Ycnt += 1

print(Xcnt, Ycnt)