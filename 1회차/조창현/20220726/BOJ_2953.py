score_sum = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0
}

for i in range(1, 6):
    score = input().split()
    for j in score:
        score_sum[i] = score_sum.get(i) + int(j)
#print(score_sum)
player_list = list(score_sum.keys())
score_list = list(score_sum.values())

position = score_list.index(max(score_sum.values()))

print(f'{player_list[position]} {max(score_sum.values())}')