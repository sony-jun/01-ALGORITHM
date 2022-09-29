# 하얀 칸 위에 말이 몇 개 있는지 출력

# 빈 리스트 생성
chess = []
# 체스판 8x8 크기
# 반복문으로 행을 받음
for _ in range(8):
    # chess에 추가
    chess.append(list(map(str, list(input()))))

answer = 0
for i in range(8):
    for j in range(8):
        # i+j가 짝수면
        if (i + j) % 2 == 0:
            # [i][j]가 말이 있는 칸이면
            if chess[i][j] == 'F':
                # 1 증가
                answer += 1
                
print(answer)