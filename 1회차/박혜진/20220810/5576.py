score = []

for _ in range(20) :
    score.append(int(input()))

    w = sorted(score[:10], reverse=True)
    k = sorted(score[10:], reverse=True)

print(sum(w[:3]), sum(k[:3]))