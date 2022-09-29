a = []
score = 0
for i in range(10):
    a.append(int(input()))
for j in a:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)