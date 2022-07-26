import sys

sys.stdin = open("3_나는_요리사다.txt")

participants_score = []
total = []

for i in range(5):
    score_list = list(map(int, input().split()))
    participants_score.append(score_list)

for ele in participants_score:
    total.append(sum(ele))

print(total.index(max(total)) + 1, (max(total)))