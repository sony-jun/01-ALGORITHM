high_score = 0
winner = 0
for i in range(1, 6):
    chef = list(map(int, input().split()))
    score = sum(chef)
    if high_score < score:
        high_score = score
        winner = i
print(winner, high_score)