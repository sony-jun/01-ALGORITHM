# https://www.acmicpc.net/problem/1100
chess = []
cnt = 0
for i in range(8):
    chess.append(list(input()))

#하얀 칸 위에 말이 몇개 있는지 출력 F:말이 있는 칸
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if chess[i][j] in 'F':
                cnt += 1 
print(cnt)
