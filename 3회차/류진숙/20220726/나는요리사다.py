
who_is_winner = []
for p in range(1, 6):
    score_list = sum(map(int, input().split()))
    who_is_winner.append([p, score_list])

win = who_is_winner[0][1]
i = who_is_winner[0][0]
for winner in who_is_winner:
    if winner[1] > win:
        win = winner[1]
        i = winner[0]

print(f'{i} {win}')