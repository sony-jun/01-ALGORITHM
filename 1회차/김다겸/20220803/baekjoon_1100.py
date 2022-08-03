matrix = [list(input()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        # 흰 체스판은 i+j가 짝수일 때이다.
        if (i + j) % 2 == 0:
            # 흰 체스판에 말이 있다면
            if matrix[i][j] == "F":
                # 개수 세기
                cnt += 1
print(cnt)