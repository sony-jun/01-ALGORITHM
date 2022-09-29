import sys

sys.stdin = open("input.txt")

# ------- 밑에 입력 --------

sum_score = []

for i in range(5):
    sum_ = sum(map(int, input().split()))
    sum_score.append(sum_)

print(sum_score.index(max(sum_score)) + 1, max(sum_score))
