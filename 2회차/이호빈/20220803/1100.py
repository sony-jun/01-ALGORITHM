chess = [list(map(str, input())) for _ in range(8)]
#말이 있는 칸을 세기 위한 변수
count = 0
#체스판은 8x8로 구성되어 있다.
for i in range(8):
    for j in range(8):
        # i + j 가 짝수고 그 위치에 말이 있다면
        if (i + j) % 2 == 0 and chess[i][j] == "F":
                count += 1

print(count)