import sys
input = sys.stdin.readline

chess = [list(input()) for _ in range(8)]

cnt = 0

for i in range(8):
    for j in range(8):
        # 하얀칸은 짝수 번째와 0번째에 위치한다.
        if (i+j) % 2 == 0: #칸의 색이 하얀 경우
            if chess[i][j] == 'F': # 하얀 칸에 말이 있는 경우
                cnt += 1

print(cnt)