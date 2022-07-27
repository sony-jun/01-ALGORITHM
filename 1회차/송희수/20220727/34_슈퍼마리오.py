import sys

sys.stdin = open("34_슈퍼마리오.txt")

m = []
score = 0
for i in range(10):
    n = int(input())
    m.append(n)
for j in m:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)

