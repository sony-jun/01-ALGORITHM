score_1 = [int(input()) for _ in range(10)]
score_2 = [int(input()) for _ in range(10)]
score_1.sort(reverse=True)
score_2.sort(reverse=True)

print(sum(score_1[0:3]), sum(score_2[0:3]))
