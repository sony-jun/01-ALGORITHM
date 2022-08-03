chess = []
for _ in range(8):      # 체스판이 8x8임.
    chess.append(list(map(str, list(input()))))
    # 체스판에 주어진 입력데이터를 리스트 함.

answer = 0
for i in range(8):
    for j in range(8):      # 8x8안에서
        if (i + j) % 2 == 0: #하얀칸일 경우(행과 열의 합이 짝수여야 한다.)
            if chess[i][j] == 'F': #F있을 경우
                answer += 1
print(answer)

# https://claude-u.tistory.com/350