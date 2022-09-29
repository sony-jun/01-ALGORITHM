import sys
sys.stdin = open("20220803/1100_하얀칸.txt")

chess = []                          # 체스판 상태
for i in range(8):
    chess.append(list(input()))     # 2차원 배열

white = 0                           # 하얀 칸에 올려진 말의 수
for i in range(8):
    for j in range(8):
        if chess[i][j] == 'F':      # 말이 올려진 칸이
            if (i+j)%2 == 0:        # 하얀 칸이면
                white += 1          # 1씩 증가

print(white)                        # 최종 개수 출력