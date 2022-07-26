# "나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.

# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

import sys

sys.stdin = open("4_나는요리사다.txt")

# num = 0
# # 딕셔너리
# total = {}
# for i in range(1,6):
#     a, b, c, d = map(int, input().split())
#     total[i] = a + b + c + d
# #print(total) # {1: 18, 2: 17, 3: 18, 4: 19, 5: 17}
# if total.values() == max(total.values()):
#     print()

num = 0
cnt = 0

for i in range(1,6):
    A = list(map(int, input().split()))
    
    if sum(A) > num:
        num = sum(A)
        cnt = i
print(cnt, num)