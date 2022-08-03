# 하얀 칸

matrix = [list(input()) for _ in range(8)]
cnt = 0
for a in range(8):
    for b in range(8):
        if (matrix[a][b] == 'F') and ((a + b) % 2 == 0):
            cnt += 1
print(cnt)