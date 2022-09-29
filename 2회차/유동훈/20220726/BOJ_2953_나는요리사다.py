# https://www.acmicpc.net/problem/2953
# 나는 요리사다

# 풀이
score_table = {}
for i in range(1,6):
    score = map(int, input().split())
    score_table[sum(score)] = i
print(score_table[max(score_table)], max(score_table))