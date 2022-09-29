# 슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.

# 슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.

# 마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.

# 버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.

import sys

sys.stdin = open("4_슈퍼마리오_input.txt")


sum_ = 0
mario = {} # 키값 : 누적합 val : |100 - 누적합|
ans = 0
for i in range(10):
    N = int(input())
    sum_ += N
    mario[sum_] =abs(100-sum_)
#print(mario) #{10: 90, 30: 70, 60: 40, 100: 0, 150: 50, 210: 110, 280: 180, 360: 260, 450: 350, 550: 450}
    for k, v in mario.items():
        if v == min(mario.values()):
            ans = k
print(ans)





















# score = []
# sum_score = []
# for t in range(10):
#     score.append(int(input()))
# #print(score) [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 리스트에 숫자 추가

# sum_plus = 0
# for plus in score:
#     sum_plus += plus
#     sum_score.append(sum_plus)
# #print(sum_score) [1, 3, 6, 11, 19, 32, 53, 87, 142, 231] 누적 합 리스트

# x = []
# for near in sum_score:
#     x.append(abs(100 - near))
# #print(x) #[99, 97, 94, 89, 81, 68, 47, 13, 42, 131] 100 - 절대값 리스트
# #print(min(x)) 13

# for i in range(1, len(x)): 
#     if x.count(min(x)) >= 2:
#         print(sum_score[i+1])
#         break
#     else:
#         print(100-min(x))
#         break