judge = []

for i in range(5) :
  judge.append(sum(map(int, input().split())))

winner = max(judge)

print(judge.index(winner) + 1, winner)