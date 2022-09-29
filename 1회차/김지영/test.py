N = int(input())
player = [0] * N

game = [list(map(int, input().split())) for i in range(N)]
# 89 92 77
# 89 92 63
# 89 63 77

for i in range(N):
    for j in range(3):
        if game[i].count(game[i][j]) >= 2:
            player[i] += 0
        else:
            player[i] += game[i][j]
for k in player:
    print(k)
