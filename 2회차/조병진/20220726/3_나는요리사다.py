# 문제 : 5명이 서로 다른 사람에게 평가점수를 주고, 우승자와 그의 점수를 구하기
# 입력 : 5 4 4 5
#       5 4 4 4
#       5 5 4 4
#       5 5 5 4
#       4 4 4 5
# 출력 : 4 19

sum_score = []

for i in range(5):
    sum_ = sum(map(int, input().split()))
    sum_score.append(sum_)

print(sum_score.index(max(sum_score)) + 1, max(sum_score))
