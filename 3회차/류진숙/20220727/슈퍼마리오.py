import sys

sys.stdin = open('슈퍼마리오.txt')


score_list = []

for i in range(10):
    score_list.append(int(input()))

sum_list = []
sum_score = 0 
for score in score_list:
    sum_score += score
    sum_list.append(sum_score)

    dif = 0
    dif_dict = {}
    for s in sum_list[::-1]:
        if s > 100:
            dif = s - 100
            dif_dict[dif] = s
        elif s == 100:
            print(s)
            break
        else:
            dif = abs(s - 100)
            min_ = min(list(dif_dict.keys()))
            if dif < min_:
                print(s)
                break
            elif dif == min_:
                print(dif_dict.get(min_))
                break

# m = []
# score = 0
# for i in range(10):
#     m.append(int(input()))
# for j in m:
#     score += j
#     if score >= 100:
#         if score - 100 > 100 - (score - j):
#             score -= j
#         break
# print(score)
