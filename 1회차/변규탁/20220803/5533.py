N = int(input())

game = [list(map(int, input().split())) for _ in range(N)]

game_set = []
for i in range(3):
    game_set.append([game[j][i] for j in range(N)]) # 첫번째행의 열방향으로 요소 하나씩


for i in range(N):
    for j in range(3):
        if game_set[j].count(game[i][j]) > 1:
            game[i][j] = 0

for i in range(N):
    print(sum(game[i]))

